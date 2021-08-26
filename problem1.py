#%%
def helper(number, left_bound, right_bound):
    '''
    Recursive function that halves the search space (of integers) for
        an integer which when squared will return number. => o(log n)
    :param number: Number to be squared.
    :param left_bound: Min integer of the search space that when squared MAY return number.
    :param right_bound: Max integer of the search space that when squared MAY return number.
    :return: final value is the floor integer of the square-root of the number.
    '''
    checkvalue = (left_bound + right_bound)//2
    checkvalue_Square = checkvalue**2

    # To handle exception case when the number is 0
    if number == 0:
        return 0

    if left_bound+1 == right_bound or left_bound == right_bound:
        return checkvalue

    if checkvalue_Square == number:
        return checkvalue
    elif checkvalue_Square < number:
        return helper(number, checkvalue, right_bound)
    elif checkvalue_Square > number:
        return helper(number, left_bound, checkvalue)

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return helper(number,1,number)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
