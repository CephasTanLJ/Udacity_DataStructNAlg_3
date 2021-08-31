#%%
def sort_012(input_list):
    '''
    left_idx tracks the location of 1st 1 and
    right_idx tracks the location of the 1st 2.
    Using the scanning_idx, this iterates over every element once O(n) and allocate (in-place)
    all 0s to the left of the 1s,
    and all 2s to the right of the 1s.
    Therefore the overall time complexity is 0(n).

    '''
    left_idx = 0
    right_idx = len(input_list) - 1
    scanning_idx = 0

    while scanning_idx <= right_idx:
        if input_list[scanning_idx] == 0:
            input_list[left_idx], input_list[scanning_idx] = input_list[scanning_idx], input_list[left_idx],
            scanning_idx += 1
            left_idx += 1

        elif input_list[scanning_idx] == 1:
            scanning_idx += 1
        elif input_list[scanning_idx] == 2:
            input_list[right_idx], input_list[scanning_idx] = input_list[scanning_idx], input_list[right_idx]
            right_idx -= 1

    return input_list


def testUdacity():
    test1 = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    test2 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    test3 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    assert sort_012(test1) == sorted(test1)
    assert sort_012(test2) == sorted(test2)
    assert sort_012(test3) == sorted(test3)

def testEdgeCase1():
    '''If input is an empty arr'''
    assert sort_012([]) == [], 'Empty array should return empty array'

def testEdgeCase2():
    '''if input only contains 0, 1 or 2'''
    assert sort_012([0,0,0,0,0]) == [0,0,0,0,0], f'Should return all 0s, but {sort_012([0,0,0,0,0])} was returned'
    assert sort_012([1 for i in range(1,10)]) == [1 for i in range(1,10)], f'Should return all 1s, but {sort_012([1 for i in range(1,10)])} was returned'
    assert sort_012([2 for i in range(1,10)]) == [2 for i in range(1,10)], f'Should return all 2s, but {sort_012([2 for i in range(1,10)])} was returned'

if __name__ == '__main__':
    testEdgeCase1()
    testEdgeCase2()
    testUdacity()
