


class NewsAnalyzer:
    """This is a class that analyze the news data

    :param data: a file that all the historical news and prices from a specific source 
    :type data: csv


    
    """
    def __init__(self, data):
        """Constructor method"""
        self.df = pd.read_csv(data)
        #TODO: delete the rows that have a Nan values
        #TODO: delete columns [title, description]



    def example(self):
        '''
        example [summary]
        '''
        pass



class Model:
  
    '''
     [summary]
    '''

    def __init__(self, name, age):
        '''
        __init__ [summary]

        :param name: [description]
        :type name: [type]
        :param age: [description]
        :type age: [type]
        '''
        self.name = name
        self.age = age