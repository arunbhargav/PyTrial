'''
Created on Mar 21, 2016

@author: arunbhargava
'''
import logging;

class MyClass(object):
    '''
    classdocs
    '''
    data = None 

    def __init__(self, data):
        '''
        Constructor
        '''
        self.data   = data
        logger = logging.getLogger(__name__)
        logger.debug()
    
    
        