from fincli.tools import *

INDEX_FORMAT = "Index Price ({})"
STOCK_FORMAT = "Stock Price ({})"

params = {
    "start_date": [2016, 8, 1],
    "end_date": [2021, 9, 1],
    "date_interval": "m",
    "stock_symbol": "TSLA",
    "index_symbol": "^GSPC"
}


def calculate_capm_values(params):
    """Function that calculates
    + r-squared
    + beta
    + alpha
    with a set of parameters
    """
    # print(params)
    column_stock = STOCK_FORMAT.format(params["stock_symbol"])
    column_index = INDEX_FORMAT.format(params["index_symbol"])


    # get an array of dates
    date_list = get_date_list(
        params["index_symbol"],
        params["start_date"],
        params["end_date"],
        interval=params["date_interval"]
    )
    # generate an empty data frame for price data
    data_frame = generate_data_frame(column_index, column_stock, date_list)
    # populate with data from yahoo finance
    populate_data_frame(data_frame, params, column_index, column_stock)
    print(data_frame.head())
    ret = generate_percent_change(data_frame)
    result = model(ret, column_index, column_stock)
    regressionPlot(ret, result, column_index, column_stock)
    return result
