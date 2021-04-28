

''' This file is to scrape the information from the internet 

Summary
----------




Functions
----------
get_news: sequence of ints
   The list of integers to sum up.

R
-------


See also
--------

'''



class Ticker:
    ''''''
    URLs = {
        'yahoo': None,
        'reuters': "https://www.reuters.com/companies/{ticker}.{market}"

    }
    def __init__(self, ticker) -> None:
        self.ticker = ticker

    def get_news(self, source='yahoo'):
        """
        This is a .

        :param source: 
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
        """
        pass

    def get_recent_news(self):
        pass

    def show_name(self):
        pass