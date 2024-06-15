'''
Created on Feb 16, 2023

@author: Rohan Chodapunedi
@attention: this is only a template
'''
import unittest
from algorithm import findTime


class functionname_test(unittest.TestCase):
    def test(self):
        arr = [10, 20, 30]
        n = 3
        x = findTime(arr, n)    
        assert(x == 60)
        print("assertion passed")
        
        arr2 = [5, 25, 30]
        n2 = 3
        x2 = findTime(arr2, n2)   
        assert(x2 == 60)
        print("assertion passed")
       

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()