def get_min_max(ints):
    '''
    Using a min_idx and max_idx to trace the location of the min value and max value
    via iterative comparison of current min and max value with each element and update
    the lower or higher value accordingly.
    Since there is 2 comparison per iteration and the array is only traverse once,
    the time complexity = O(2n) ~ O(n)

    :param ints: an array of integers
    :return: (min integer, max integer)
    '''
    if len(ints) == 0:
        return None

    min_idx = 0
    max_idx = 0

    for idx, elem in enumerate(ints):
        if type(elem) is not int:
            continue
        if ints[max_idx] < elem:
            max_idx = idx
        if ints[min_idx] > elem:
            min_idx = idx

    return ints[min_idx], ints[max_idx]



def testUdacity():
    ints = [5, 8, 4, 2, 7, 9, 1, 0, 3, 6]
    assert get_min_max(ints) == (0, 9)

def edgeCase1():
    '''If ints is an ampty array.'''
    assert get_min_max([]) == None

def edgeCase2():
    '''if non-integer is given. Ignore that element.'''
    ints = [5, 8, 4, 2, 7, 9, 1, 0, 3, 6, 'A']
    assert get_min_max(ints) == (0, 9)

if __name__ == '__main__':
    testUdacity()
    edgeCase1()
    edgeCase2()

