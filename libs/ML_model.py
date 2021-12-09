from libs.get_data import Ticker

# from fbprophet import Prophet
import numpy as np
import pandas as pd


class ML_model_prophet(Ticker):
    """
    This model uses the model called "prophet" from facebook

    :param Ticker: the ticker of a comany in the stock market
    :type Ticker: str
    """

    def __init__(self, df_ticker):
        self.df = df_ticker


def predict_price(data, ticker):
    # get data for a specific ticker
    # data = pd.read_csv(data, low_memory=False)
    ticker_data = data[data["ticker"] == ticker]

    # sort the data from recent to oldest
    ticker_data.sort_values(by=["date"], inplace=True, ascending=False)

    # clean data and get rid of not values
    ticker_data.dropna(subset=["polarity"], inplace=True)

    # get polarities and convert them to numpay array for speed
    polarity = ticker_data["polarity"].values
    polarity = np.array(polarity, dtype=np.float32)

    # calculate average of the past 5 polarities
    average = np.average(polarity[0:3])
    print(average)

    if average > 0.1:
        return "Positive: price wil increase"
    elif average <= 0.1 or average >= -0.1:
        return "Neutral: cannot predict price"
    else:
        return "Negative: price wil Decrease"
