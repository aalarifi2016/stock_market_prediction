from libs.get_data import Ticker
from fbprophet import Prophet


class ML_model_prophet(Ticker):
    """
    This model uses the model called "prophet" from facebook

    :param Ticker: the ticker of a comany in the stock market
    :type Ticker: str
    """

    def __init__(self, df_ticker):
        self.df = df_ticker
