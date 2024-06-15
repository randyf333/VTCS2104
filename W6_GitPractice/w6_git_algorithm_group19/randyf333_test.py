'''
Created on Feb 16, 2023

@author: siwei cao
@attention: this is only a template
'''
import unittest
from algorithm import findTime


class functionname_test(unittest.TestCase):
    def test(self):
        #declare needed variables for testing    
        arr = [10,20,30]
        num = 3
        #assert statements such as 
        #self.assertEqual(<function call>,<expected output>)
        # or self.assertTrue(a==b)
        self.assertEqual(findTime(arr,num),60)

        arr2 = [1,2,5,8]
        num2 = 4
        self.assertEqual(findTime(arr2,num2),15)

       


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()