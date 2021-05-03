

''' The get_data module is to scrape the information from the internet 

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

'''

from bs4 import BeautifulSoup
import requests


class Ticker:
    
    """
     [summary]

    [extended_summary]
    """



    _URLs_news = {
        'yahoo': None,
        'reuters': "https://www.reuters.com/companies/{ticker}.{market}"

    
    }
    _URLs_stock_prices = {
        'yahoo': "https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start_date}&period2={end_date}&interval=1d&events=history&includeAdjustedClose=true",
    }
    
    def __init__(self, ticker) -> None:
        """
        __init__ class constructor

        [extended_summary]

        :param ticker: the symbol of a company's name in the stock market 
        :type ticker: str
        """
        self.ticker = ticker

    def get_news(self, source='yahoo') -> list:
        """
        get_news [summary]

        [extended_summary]

        :param source: [description], defaults to 'yahoo'
        :type source: str, optional
        
        :returns: list of all 
        :rtype: str
        
        :raises ValueError: when source is not valid 
        
        :Example:
        
        >>> import os 
        """
        
        results = []
        if source == 'yahoo': 
            pass 
        
        elif source == 'reuters': 
            # NOTE: there are two options for the markets in the reuters website which are:
            # OQ -> represent NASDAQ
            # N -> represent the NYSE (New York Stok Exchange)
            # this code will check both markets to find which market the ticker is in 
            markets = ['N', 'OQ']
            for market in markets:
                url = _URLs_news['reuters'].format(self.ticker, market)
                
            
        else:
            raise ValueError('the source ' + source + 'is not recognized')
        
    def _scrapping_reuters_news(self, ticker, market) -> list:
        
        """
        a function that scrape the news from reuters

        the news in reuters is in a list and once the user reach the end of the page, 
        the page will load more content if it has until all the news in its database is shown.
        in order to get all the news, this function will try to mimic the behavior of the user
        (using Selenium) and scroll until the there is no more news, then use parsing library
        like: beatifulsoup to get all the news 
        """
        
        pass
    
    
    def get_recent_news(self, source='yahoo') -> list:
        """
        get_recent_news [summary]

        [extended_summary]

        :param source: [description], defaults to 'yahoo'
        :type source: str, optional
        :raises ValueError: [description]
        :return: [description]
        :rtype: list
        """
        url = ''
        if source == 'yahoo':
            #TODO: write a code to get the recent news from yahoo
            pass
            
        elif source == 'reuters':
            for market in ['OQ', 'N']:
                url = self._URLs_news['reuters'].format(self.ticker, market)
                page = requests.get(url)
                soup = BeautifulSoup(page, 'html.parser')
                
                news_list = soup.findall('div', {'class': 'item'})
                news_urls = {}
                
                for news in news_list:
                    news_urls.append({
                                        'title': news.div.a.text,
                                        'description': news.div.p.text,    
                                        'link': news.div.a["href"]
                    })
                                     
                if len(news_urls) > 2 :
                    return news_urls
                      
                      
            
            return []
                    
                    
                
                
        
        else:
            raise ValueError('the source' + source + 'is not recognized')

    def show_name(self):
        """
        a function that returns the name of the ticker's company

        
        """
        pass
    
    
    
    def historical_data(self, tickers, t1, t2, options='show'):
        """
        download_historical_data [summary]

        [extended_summary]

        :param tickers: [description]
        :type tickers: [type]
        :param t1: [description]
        :type t1: [type]
        :param t2: [description]
        :type t2: [type]
        """
        # tickers (list) -> a list of the tickers needed to be downloaded
        # t1 (int) -> the starting date in seconds
        # t2 (int) -> the ending date in seconds
    
                
        # download the data 
        path = f'{ticker}/historical_data.csv'
        if not os.path.isfile(f'{ticker}/historical_data.csv'):
            url = get_url(ticker, t1, t2)
            
            print('Beginning file download with wget module', end=' ')
            
            try:
                wget.download(url, path)
                print(" .... success")
                
            except:
                print(" .... failed")
                
                
            time.sleep(4)