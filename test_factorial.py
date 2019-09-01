import unittest     # Import the Python unit testing framework
import maths        # Our code to test

class factorialTest(unittest.TestCase):
    ''' Unit tests for our factorial functions. '''
    
    def test_factorial(self):
        ''' Tests the factorial function. '''
        t = maths.factorial(5)
        
        self.assertEqual(t,120)

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
