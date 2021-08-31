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
    if type(number) is not int:
        #Enforce the input number is an integer
        return None
    return helper(number,1,number)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

def test1():
    '''Edge Case 1: number is not an integer'''
    assert sqrt('N') == None, 'non integer number was accepted into function!'

def test2():
    '''Edge Case 2: When number is 0 or 1, the function should return 0 and 1 respectively.'''
    assert sqrt(0) == 0, f'Function should return 0 but {sqrt(0)} was returned'
    assert sqrt(1) == 1, f'Function should return 0 but {sqrt(1)} was returned'

def testUdacity():
    assert sqrt(9) == 3, 'fail'
    assert sqrt(0) == 0, 'fail'
    assert sqrt(16) == 4, 'fail'
    assert sqrt(1) == 1, 'fail'
    assert sqrt(27) == 5, 'fail'

if __name__ == '__main__':
    test1()
    test2()
    testUdacity()
