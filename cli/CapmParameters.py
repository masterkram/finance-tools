def format_date(date):
    return "{}, {}, {}".format(date[2], date[1], date[0])


class CAPMParameters():
    """CAPM parameters class"""
    def __init__(self, start_date, end_date, date_interval, stock_symbol, index_symbol):
        self.start_date = start_date
        self.end_date = end_date
        self.date_interval = date_interval
        self.stock_symbol = stock_symbol
        self.index_symbol = index_symbol

    def to_string(self):
        return ('CAPM Parameters\n'
                + 'from {} to {}\n'.format(format_date(self.start_date), format_date(self.end_date))
                + 'with interval {}\n'.format(self.date_interval)
                + 'stock: {} | index: {}'.format(self.stock_symbol, self.index_symbol)
                )

    def to_dict(self):
        return {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "date_interval": self.date_interval,
            "stock_symbol": self.stock_symbol,
            "index_symbol": self.index_symbol
        }