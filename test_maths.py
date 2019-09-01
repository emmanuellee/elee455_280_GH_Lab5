import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        t = maths.add(1,2)
        t2 = maths.add(10,2,0)
        
        self.assertEqual(t,3)
        self.assertEqual(t2,'1010')

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        t = maths.fibonacci(5)
        
        self.assertEqual(t,5)

    def test_convert_base(self):
        ''' Tests the convert_base function. '''
        t1 = maths.convert_base(10, 2)
        t2 = maths.convert_base(10, 15)
        
        self.assertEqual(t1,'1010')
        self.assertEqual(t2,'A')
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
