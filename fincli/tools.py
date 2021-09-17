import pandas as pd
import pandas_datareader as web
import datetime
import statsmodels.api as sm
import matplotlib.pyplot as plt
import time
plt.style.use('fivethirtyeight')


def read_price_data(stock_symbol, start_date, end_date, interval):
    """Import price data from Yahoo Finance"""
    try:
        stock_data = web.get_data_yahoo(stock_symbol, start_date, end_date, interval=interval)
    except:
        return None

    prices = stock_data.loc[:, "Adj Close"]
    prices = prices.fillna(method="ffill")

    return prices


def get_date_list(stock_symbol, start_date, end_date, interval):
    """Generate list of trading dates"""
    stock_data = web.get_data_yahoo(stock_symbol, start_date, end_date, interval=interval)
    dates = stock_data.index

    return dates


def generate_data_frame(column_index, column_stock, date_list):
    """Generate an empty dataframe to hold the stock and index prices"""
    column_header_index = column_index
    column_header_stock = column_stock
    df = pd.DataFrame(
        columns=[column_header_index, column_header_stock], index=date_list
    )

    # Sort dataframe based on date
    df = df.sort_index(ascending=False)
    return df


def populate_data_frame(df, params, column_index, column_stock):
    try:
        price_series = read_price_data(
            params["index_symbol"],
            params["start_date"],
            params["end_date"],
            interval=params["date_interval"]
        )
        df[column_index] = price_series

        price_series = read_price_data(
            params["stock_symbol"],
            params["start_date"],
            params["end_date"],
            interval=params["date_interval"]
        )
        df[column_stock] = price_series
    except:
        print('Import failed')


def generate_percent_change(df):
    mtl_ret = df.resample('M').mean().pct_change(fill_method='ffill')
    mtl_ret = mtl_ret.dropna(axis=0)
    return mtl_ret


def model(df, column_index, column_stock):
    x = df[column_index]
    y = df[column_stock]

    x_sm = sm.add_constant(x)
    regression = sm.OLS(y, x_sm)
    results = regression.fit()
    return {"alpha": results.params[0], "beta": results.params[1], "r-squared": results.rsquared}


def regressionPlot(df, params, column_index, column_stock):
    plt.scatter(df[column_index], df[column_stock], marker='o')
    plt.plot(df[column_index], params["beta"]*df[column_index] + params["alpha"])
    plt.xlabel(column_stock)
    plt.ylabel(column_index)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = 'img/CAPM-{}.png'.format(timestr)
    plt.savefig(filename, bbox_inches='tight')
    print("saved regression plot at {}".format(filename))