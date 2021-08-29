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

    min_idx = 0
    max_idx = 0

    for idx, elem in enumerate(ints):
        if ints[max_idx] < elem:
            max_idx = idx
        if ints[min_idx] > elem:
            min_idx = idx

    return ints[min_idx], ints[max_idx]


ints = [5, 8, 4, 2, 7, 9, 1, 0, 3, 6]

get_min_max(ints)