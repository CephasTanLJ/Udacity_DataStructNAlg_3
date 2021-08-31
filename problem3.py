def mergesort(array):
    '''
    Merge sort recursively divides the data set to sort
    uses and iteratively merge the elements of each halved data set.
    Therefore the time complexity is O(nlog(n) ).
    :param array:
    :return:
    '''
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_arr = array[:mid]
    right_arr = array[mid:]

    left_arr = mergesort(left_arr)
    right_arr = mergesort(right_arr)

    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    merge_arr = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            merge_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merge_arr.append(right_arr[right_idx])
            right_idx += 1

    merge_arr += left_arr[left_idx:]
    merge_arr += right_arr[right_idx:]

    return merge_arr


def assign(sorted_array):
    left_placeholder = 1
    right_placeholder = 1
    output = [0,0]
    for idx, value in enumerate(sorted_array):
        if idx % 2 != 0:
            output[0] += left_placeholder*value
            left_placeholder *= 10
        else:
            output[1] += right_placeholder*value
            right_placeholder *= 10
    return output

sum(assign([1,2,3,4,5]))

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    First the array is sorted via merge sort O(nlog(n) ).
    Next, each elements is iteratively assigned to either the left or the right number of the final
    list in an alternating manner o(n). After each assignment, the number place holders is increased
    by multiplying the current value by 10. This allows the next assigned value to that number to be
    added into number without changing the current digits.

    Since the 2 operations are independent from each other O(nlog(n) ) + O(n) = O(nlog(n) )
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    sorted_array = mergesort(input_list)
    return assign(sorted_array)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
