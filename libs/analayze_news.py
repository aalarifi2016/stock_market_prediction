""" This file  

Summary
----------
This library is 



Functions
----------
example: seq
   The .
   

R
-------


See also
--------

"""

import pandas as pd


class NewsAnalyzer:

    """This is a class that analyze the news data

    :param data: a file that all the historical news and prices from a specific source
    :type data: csv



    """

    def __init__(self, source_file="../csv_data/reuters_news.csv"):
        """
        class constructor

        :param source_file: [description], defaults to '../csv_data/reuters_news.csv'
        :type source_file: str, optional
        """

        self.df = pd.read_csv(source_file)
        # TODO: delete the rows that have a Nan values
        # TODO: delete columns [title, description]

    def name(self, args):

        pass
