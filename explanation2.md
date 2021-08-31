# Problem 2: Search in a Rotated Sorted Array 
by Cephas Tan Li-Jie
## Assignment description
You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
You are given a target value to search. If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

## Method of implementation
A `minIdxFinder()` function is first applied to the array to obtain the index of the minimum value of the array. 
This recursive function works with a `O(log(n))`time complexity because it halves
the search space within each recursive step to obtain the min function - a similar algorithm used in Problem 1 function.

With the min value of the array identified, the array can now be divided into two possible search spaces:
the numbers before the min index and the numbers from the min index till the end of the array.
The determining factor on which search space the input number falls in is decided by the last element of the array.
If the input number is less than the last element, the search space will start from the min_idx to the last element.
On the otherhand, if the input number is more the the last element, the search space from be the numbers before the 
min index. Using this properties, the `searchlist()` function recursively halve the current search space to find the 
final number. This is a similar method to the minIdxFinder(). Therefore it has a time complexity of `O(log(n))`.

Overall, since `minIdxFinder()` is applied independently from `searchlist()` in the `rotated_array_search()` function , 
the time complexity is `O(2*log(n))`which is the same as `O(log(n))`.

Variables are reassigned/reused at each recursive step of each function. Therefore, the algorithm has a constant space 
complexity.

Time complexity = `O(log(n))`\
Space complexity = `O(1)`

## Functions used
1. `minIdxFinder()`  - helper function
2. `searchlist()` - helper function
3. `rotated_array_search()` - final function that combines the first two finctions to solve the problem.


