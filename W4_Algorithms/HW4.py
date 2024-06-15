"""
@date: <date here>
@author: Randy Fu
@PID: randyf333
@assignment: Week 4 Homework
@note: Do NOT alter the function headers that are well documented, 
Do put your hw answers in the spaces provided within function headers
"""


def log_base_2(number: float) -> str:

    """ Gives the approximate log base 2 calculation of the input number
    @param number: float to calculate on
    @precondition: number is > 0
    @return str: A string description of the approximate result
    parts i-iii from HW
    i. Work out the steps to figure out the 2 concrete examples of 256 and 81
     step by step and briefly explain your work and thinking(5pts)
     
     256 is 2^8, therefore I can count the number of times 256 is divided by 2 until I end up with a number 
     that is 2 or less, and I can count how many times I divided by 2. With 81, I have to track a lower and upper bound
     to figure out between what numbers they fall between. 
     
     ii. Find and describe a pattern and attempt to generalize (5pts)

     If my number is greater than or equal to 2, then divide by 2 and add one to the count. If the number ends up being 1 (power of two)
     then return the result. Otherwise, count until the number is less than 2, this is the lower bound and then add 1 to get the upper 
     bound. If the number is already less than 2, I multiply by 2 and keep track of the number of times I multiply by 2 until I reach 
     1 or go over, but instead I subtract instead of add to the count. 
    
	iii. Investigate and explain special cases to see if the pattern holds up (5pts)

    number = 1 returns 0
    number = 2 returns 1
    number = 0.5 returns -1
    """
    if number <= 0:
        return "Number less than 0"

    result = 0 

    if number < 2:
        while number < 1:
            result -= 1
            number *= 2
    else:
        while number >= 2:
            number /= 2
            result += 1
    
    if number == 1:
            return str(result)       
    return "between " + str (result) + " and " + str(result+1)

    
    



def reverse_list(aList: list) -> list:
    """Gives a list with the elements in reversed order
    @param aList: list input that's going to be reversed
    @return list: the reversed version of the input list
    parts i-iii from HW
    i. Work out the steps to figure out a concrete example and briefly explain
     your work and thinking(5pts)

    Swapping the input list requires that I track indexes of the beginning and the end of the list. An example would be 
    for the list [1,2,3,4,5] and having one variable track the first index (0) and another variable track the last index (4).
    Then, I swap the values at the two indexes and then iterate them. So the first variable would be 1 and the other variable 
    be 3. Then I keep going until the first variable is greater than or equal to the second variable  

	ii. Find and describe a pattern and attempt to generalize (5pts)

    With int first storing the first index and int last storing the last index, have a temporary variable to help swap the values at 
    those indexes. Then, add one to variable first and subtract one from variable last. Continue this process until the variables are 
    equal or overlap. 

	iii. Investigate and explain special cases to see if the pattern holds up (5pts)

    [0] first and last are the same, so no swap is made
    [0,1] first = 0, last = 1. The numbers swap and then first = 1 and last = 0. first > last so the loop stops. 
    [] list just returns empty list
    """
    temp = 0
    first = 0
    last = len(aList)-1
    while(first < last):
        temp = aList[last]
        aList[last] = aList[first]
        aList[first] = temp
        first+=1
        last-=1
    return aList
