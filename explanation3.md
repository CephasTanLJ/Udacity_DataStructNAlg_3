# Problem 3: Rearrange Array Elements
by Cephas Tan Li-Jie
## Assignment description
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

For e.g. [1, 2, 3, 4, 5].

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

## Method of implementation
Since the desired time complexity is `O(nlog(n))`, an appropriate algorithm to use is mergesort. The `mergesort()`function
recursively halves the array to its constituent elements, before recursively merging the elements (while sorting in the process).

After this inplace sorting (mergesort), the `assign()` function is applied. This function creates a 2 element output list.
Both left and right element of the output list starts at 0. Next, each alternating element of the sorted array is multiplied by a `placeholder`
variable before adding to either the left or the right element of this list.
The placeholder determines if the next available "space" in either element of the list is in the "ones", "tens", "thousands".
The assignment process dependents on the number of elements in the input array. Therefore, the time complexity of this function is `O(n)`.\
*Note that each element of the output list has its own placeholder variable(e.g., `left_placeholder` and `right_placeholder`). 

Overall, 2 function operates independently and the time complexity is `O(nlog(n) + n)` + `O(n)`which is the same as `O(n*log(n))`.

The mergesort is an inplace sorting mechanism which means the space complexity is for the `mergesort()` is O(1). 
Similarly, the `assign()`function only creates a single output list and the reassignment process
mutates the same element within the list. This means that the space complexity is also O(1).

Time complexity = `O(nlog(n))`\
Space complexity = `O(1)`

## Functions used
1) `mergesort()`
2) `merge()` - helper function of `mergesort()`
3) `assign()`
4) `rearrange_digits()` - function that used the above function to solve the problem.