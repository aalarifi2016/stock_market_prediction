# import pytest
# import pandas as pd
# from pandas._testing import assert_frame_equal
# from libs.get_data import Ticker
# from datetime import datetime
# import io


# def test_historical_data():
#     data = io.StringIO(
#         """Date,Open,High,Low,Close,Adj Close,Volume
#             2019-01-02,38.7225,39.712502,38.557499,39.48,38.505024,148158800
#             2019-01-03,35.994999,36.43,35.5,35.547501,34.66964,365248800"""
#     )
#     pd.options.display.max_rows = None
#     pd.options.display.max_columns = None
#     expected = pd.read_csv(data, sep=",")
#     expected["Date"] = expected["Date"].str.replace(" ", "")
#     results = Ticker("AAPL")._historical_data(
#         datetime(2019, 1, 1), datetime(2019, 1, 4)
#     )
#     # deleting adj close value because it is always changing
#     del expected["Adj Close"]
#     del results["Adj Close"]
#     assert_frame_equal(expected, results)
