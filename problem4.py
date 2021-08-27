#%%
def sort_012(input_list):
    '''
    left_idx tracks the location of 1st 1 and
    right_idx tracks the location of the last 1.
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


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

