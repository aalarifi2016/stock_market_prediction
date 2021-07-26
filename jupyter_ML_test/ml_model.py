import numpy as np
from scipy.sparse import data
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd
from sklearn.linear_model import LinearRegression


class model:
    """
    This class will use multiple linear regression technique to predict the price of a stock company in the near future

    """

    def __init__(self, ticker):
        """
        initialize the data by filtering the news based on the ticker

        :param ticker: the ticker of the company
        :type ticker: str
        """

        self.ticker = ticker
        self.all_data = pd.read_csv("../csv_data/reuters_news.csv", low_memory=False)
        self.data = self.all_data.loc[self.all_data["ticker"] == self.ticker]
        self.data = self.data.dropna(axis=0)

        # TODO: test if there is an information about the ticker (if self.data is empty)

    def _setup_data(self):
        # separate the given data from  the target
        x = self.data[["polarity", "subjectivity"]]
        y = self.data["prices"]

        # split the data
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, random_state=42
        )

        return {
            "x_train": x_train,
            "x_test": x_test,
            "y_train": y_train,
            "y_test": y_test,
        }

    def predict(self):
        # get the split data
        data = self._setup_data()

        # define the model
        linear_regression = LinearRegression()

        # fit the model
        linear_regression.fit(data["x_train"], data["y_train"])

        # predict
        y_prediction = linear_regression.predict(data["x_test"])

        # calculate the accuracy of the prediction
        score = r2_score(data["y_test"], y_prediction)
        mean_sqrd_error = mean_squared_error(data["y_test"], y_prediction)
        root_mean_sqrd_error = np.sqrt(mean_sqrd_error)
        return {
            "y_predict": y_prediction,
            "score": score,
            "mean_sqrd_error": mean_sqrd_error,
            "root_mean_sqrd_error": root_mean_sqrd_error,
        }


if __name__ == "__main__":
    p = model("AAPL")
    print(p.predict()["root_mean_sqrd_error"])
