'''
Created on Mar 21, 2016

@author: arunbhargava
'''
import logging

LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MyClass():
    data = None
    def __init__(self, data):
        self.data   = data

if __name__ == "__main__":
    a = MyClass("Data")
    logger.info("This is message")
    

        