"""
@date: 2/21
@author: Randy Fu
@PID: randyf333
@assignment: Week 6 Homework
@note: Do NOT alter the function headers that are well documented
"""

def sum_digits(number: int) -> int:
    """ Sums each digit of a number together using recursion
    @param number: an integer whose digits will be summed
    @return: the sum of all digits in the number
    """
    num = abs(number)
    if num == 0:
        return 0
    digit = num%10
    return digit+sum_digits(num//10)



def is_diff_two(values: list, diff: int) -> bool:
    """ Checks if there are two elements within a list that have a specific difference between them using recursion 
    @param values: The list of integer values to be searched
    @param diff: The difference value between two elements to find
    @return: True if there are two elements in values with a difference of diff, otherwise False
    """
    if len(values) < 2:
        return False
    return diff_helper(values,diff,0,1)

def diff_helper(values: list, diff: int, index1: int, index2: int) -> bool:
    if index1 == len(values)-1 and index2 == len(values):
        return False
    if abs(values[index2] - values[index1]) == diff:
        return True
    if index2 < len(values)-1:
        return diff_helper(values,diff,index1,index2+1)
    elif index1 < len(values)-2:
        return diff_helper(values,diff,index1+1,index1+2)
    
    return diff_helper(values,diff,index1+1,index1+2)

	