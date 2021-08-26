
'''
Helper functions:
minIdxFinder(): Find the index of the min value recursively by halving the search space O(log n).
searchlist():   Find the number in the inputlist also recursively by halving the given constrained inputlist.

Overall:
    Time complexity:
    min_idx (minIdxFinder() output) and its max_idx (min_idx-1) is used to divide the inputlist search space.
    The resultant search space is either inputlist[leftMostIdx:max_idx] vs inputlist[leftMostIdx:max_idx].
    To check which search space to use, compare the number to the left and right most elements of the input list.
    if number is less than right most element, then starting search space will be inputlist[leftMostIdx:max_idx];
    number more than left most element, then the starting search space will be inputlist[leftMostIdx:max_idx].

    Since minIdxFinder() and searchlist() are independently carried out from each other, the time complexity is
    O(log(n) ) + O(log(n) ) ~> O(log(n) )

    Space complexity:
    In terms of space complexity, assuming that the explicit creation of variables in my code are removed,
    there is no creation of new dataStructures ~> O(n).
    * explicit code such as mid_value can be removed and can instead be implicitly called with inputlist(mid_value),
    but explicit code are kept the algorithm more interpretable and traceable.

'''

def minIdxFinder(input_list, left_bound, right_bound):

    mid_idx = (left_bound + right_bound) // 2

    leftmost_value = input_list[0]
    rightmost_value = input_list[-1]
    mid_value = input_list[mid_idx]

    if mid_value < rightmost_value:
        check_idx = mid_idx-1
        check_value = input_list[check_idx]
        if check_value > mid_value:
            return mid_idx
        else:
            return minIdxFinder(input_list, left_bound, check_idx)
    elif mid_value > leftmost_value:
        check_idx = mid_idx + 1
        check_value = input_list[check_idx]
        if check_idx < mid_value:
            return check_idx
        else:
            return minIdxFinder(input_list, mid_idx+1, right_bound)

def searchlist(input_list, number, left_bound, right_bound):

    if left_bound > right_bound:
        return -1

    mid_idx = (left_bound+right_bound)//2

    mid_value = input_list[mid_idx]

    if number == mid_value:
        return mid_idx
    elif number < mid_value:
        return searchlist(input_list, number, left_bound, mid_idx-1)
    elif number > mid_value:
        return searchlist(input_list, number, mid_idx+1, right_bound)


def rotated_array_search(input_list, number):
    last_idx = len(input_list)-1
    min_idx = minIdxFinder(input_list,0,last_idx)   # index of the min value
    max_idx = min_idx - 1                           # index of the max value
    if number <= input_list[-1]:
        return searchlist(input_list, number, min_idx, last_idx)
    elif number >= input_list[0]:
        return searchlist(input_list, number, 0, max_idx)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])