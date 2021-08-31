# Problem 6: Max and Min in a Unsorted Array
by Cephas Tan Li-Jie
## Assignment description
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max

## Method of implementation
Using a `min_idx` and `max_idx` to trace the location of the min value and max value via iterative comparison of current min and max value with each element and update 
the lower or higher value accordingly. Since there is 2 comparison per iteration and the array is only traverse once,
the time complexity is O(2n) which is O(n).\
The variables are reused/reassigned. Therefore, the Space complexity is constant.

Time complexity = `O(n)`\
Space complexity = `O(1)`
