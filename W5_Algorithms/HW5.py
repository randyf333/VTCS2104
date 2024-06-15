"""
@date: 2/13
@author: Randy Fu
@PID: randyf333
@assignment: W5_Algorithms
@note: Do NOT alter the function headers that are well documented
"""


def max_difference(values: list) -> float:
    """ Efficiently finds the largest difference between any two elements in a list
    @param values: a list of numbers
    @return number for the largest difference between elements
    """
    min = max = values[0]
    for i in range(len(values)):
        if values[i] < min:
            min = values[i]
        if values[i] > max:
            max = values[i]
    return max-min




def sort_bivalued(values: list) -> list:
    """Efficiently sort a list of binary values
    @param values: a list of binary digits (0 or 1)
    @return: a list of binary numbers in ascending sort order
    """
    left_index = 0
    for i in range(len(values)):
        if values[i] == 0:
            values[i], values[left_index] = values[left_index], values[i]
            left_index += 1
    return values
    

