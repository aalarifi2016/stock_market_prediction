

''' This file  

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

'''


class NewsAnalyzer:
    """This is a class that analyze the news data

    :param data: a file that all the historical news and prices from a specific source 
    :type data: csv


    
    """
    def __init__(self, data):
        """
        __init__ constructor


        :param data: [description]
        :type data: .csv file
        """
        self.df = pd.read_csv(data)
        #TODO: delete the rows that have a Nan values
        #TODO: delete columns [title, description]



    def example(self):
        '''
        example [summary]
        '''
        pass


def example(self):
    """
    example [summary]

    [extended_summary]
    """
    pass





    