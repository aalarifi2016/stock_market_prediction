""" The get_data module is to scrape the information from the internet 

Overview
----------
This module is responsible to supply the program with the data it needs which are
the companies prices in the stock market and their news. 



Functions
----------
get_news: sequence of ints
   The list of integers to sum up.
   

R
-------


See also
--------

"""

from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
import pandas as pd
from pandas_datareader import data as pd_dr


class Ticker:
    """
     this class

    [extended_summary]
    """

    _URLs_news = {
        "yahoo": "https://finance.yahoo.com/quote/{}?p={}",
        "reuters": "https://www.reuters.com/companies/{}.{}",
    }
    _URLs_stock_prices = {
        "yahoo": "https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true",
    }

    def __init__(self, ticker) -> None:
        """
        __init__ class constructor

        [extended_summary]

        :param ticker: the symbol of a company's name in the stock market
        :type ticker: str
        """

        self.ticker = ticker
        response = requests.get(self._URLs_news["yahoo"].format(ticker, ticker))
        soup = BeautifulSoup(response.content, "lxml")
        # print(soup)
        self.price = float(
            soup.find("span", "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text.replace(
                ",", ""
            )
        )

        self.name = soup.find("h1", "D(ib) Fz(18px)").text.split("(")[0].strip()

    def _update_news_file(self, source="yahoo"):
        """
        [summary]

        [extended_summary]

        :param source: [description], defaults to 'yahoo'
        :type source: str, optional

        :returns: list of all
        :rtype: str

        :raises ValueError: when source is not valid

        :Example:

        >>>
        """

        results = []
        if source == "yahoo":
            # TODO: add news crawling from yahoo
            pass

        elif source == "reuters":
            # NOTE: there are two options for the markets in the reuters website which are:
            # OQ -> represent NASDAQ
            # N -> represent the NYSE (New York Stock Exchange)
            # this code will check both markets to find which market the ticker is in
            markets = ["N", "OQ"]
            for market in markets:
                url = self._URLs_news["reuters"].format(self.ticker, market)

        else:
            raise ValueError("the source " + source + "is not recognized")

    def _scrapping_reuters_news(self, market):
        """
        a function that scrape the news from reuters

        the news in reuters is in a list and once the user reach the end of the page,
        the page will load more content if it has until all the news in its database is shown.
        in order to get all the news, this function will try to mimic the behavior of the user
        (using Selenium) and scroll until the there is no more news, then use parsing library
        like: Beatifulsoup to get all the news
        """

        pass

    def _scraping_yahoo_news(self):
        pass

    def get_recent_news(self, source="yahoo"):
        """
        a function to get the recent news of a company.

        [extended_summary]

        :param source: the source (website) to get the news from. defaults to 'yahoo'
        :options:
            - 'yahoo'
            - 'reuters'
        :type source: str, optional

        :raises ValueError: if the source option is not recognized
        :return: [description]
        :rtype: list

        :example:
        .. highlight:: python
        .. code-block:: python

            Ticker('AAPL').get_recent_news(source='reuters')[0]
            >>> {'description': 'Apple Inc said on Monday it has hired former distinguished '
                'Google scientist Samy Bengio, who left the search giant amid '
                'turmoil in its artificial intelligence research department.',
                'link': 'https://www.reuters.com/article/us-apple-research/apple-hires-ex-google-ai-scientist-who-resigned-after-colleagues-firings-idUSKBN2CK1MN',
                'title': "Apple hires ex-Google AI scientist who resigned after colleagues' "'firings'}
        """

        url = ""
        if source == "yahoo":
            # TODO: write a code to get the recent news from yahoo
            pass

        elif source == "reuters":
            for market in ["OQ", "N"]:
                url = self._URLs_news["reuters"].format(self.ticker, market)
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")

                news_list = soup.find_all("div", {"class": "item"})
                news_urls = []

                for news in news_list:
                    news_urls.append(
                        {
                            "title": news.div.a.text,
                            "description": news.div.p.text,
                            "link": news.div.a["href"],
                        }
                    )

                if len(news_urls) > 2:
                    return news_urls

            return []

        else:
            raise ValueError("the source" + source + "is not recognized")

    def __str__(self):
        """
        a function that returns the name of the ticker's company


        """

    def _historical_data(self, t1, t2, method="scraping"):
        """
        [summary]

        :param t1: the starting date in seconds
        :type t1: int
        :param t2: the ending date in seconds
        :type t2: int
        :param options: [description], defaults to 'show'
        :type options: str, optional
        """

        # tickers (list) -> a list of the tickers needed to be downloaded
        # t1 (int) -> the starting date in seconds
        # t2 (int) -> the ending date in seconds
        if method == "scraping":
            # convert the dates to seconds
            t1 = time.mktime(t1.timetuple())
            t2 = time.mktime(t2.timetuple())

            # setup the url
            url = self._URLs_stock_prices["yahoo"].format(self.ticker, int(t1), int(t2))
            # read the data into a pandas.dataframe
            pd.options.display.max_rows = None
            pd.options.display.max_columns = None
            df = pd.read_csv(url)
            df.to_csv("example.txt", index=False)

            return df
        elif method == "pandas":
            return pd_dr.DataReader(self.ticker, data_source="yahoo", start=t1, end=t2)

    def get_price(self):
        return self.price


if __name__ == "__main__":
    #     time_1 = datetime(2019, 1,1)
    #     time_2 = datetime(2020, 1,1)
    # print(
    #     Ticker("AAPL")._historical_data(
    #         datetime(2019, 1, 1),
    #         datetime(2020, 1, 1),
    #         method="scraping",
    #     )
    # )
    a = Ticker("GOOG")
    print(a.get_price())
