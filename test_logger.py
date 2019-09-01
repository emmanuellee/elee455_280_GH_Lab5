import unittest
from logger import Logger

class LoggerTest(unittest.TestCase):
    ''' Unit tests for our logger functions. '''
    
    def setUp(self):
        self.target = Logger                                  
        self.logger1 = Logger()
        self.logger2 = Logger(self.target)
        
    def test___init__(self):  
        ''' Unit tests for our Initializer. '''                          
        #Arrange
        # @setUp
        
        #Act
        init1 = self.logger1._target
        init2 = self.logger2._target
        
        #Assert
        self.assertEqual(init1,self.logger1._to_console)
        self.assertEqual(init2,self.target)
         
    def test_info(self):
        ''' Unit tests for our info functions. '''
        #Arrange
        text = "Information to be logged."
        
        #Act
        info1 = self.logger1.info(text)
        info2 = self.logger2.info(text)
        
        #Assert
        self.assertEqual(info1,None)
        self.assertEqual(info2,None)
    
    def test_error(self):
        ''' Unit tests for our error functions. '''
        #Arrange
        text = "Error Message"
        
        #Act
        error1 = self.logger1.error(text)
        error2 = self.logger2.error(text)
        
        #Assert
        self.assertEqual(error1,None)
        self.assertEqual(error2,None)
        
if __name__ == '__main__':
    unittest.main()
