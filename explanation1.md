# Problem 1: Finding the Square Root of an Integer
by Cephas Tan Li-Jie
## Assignment description
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is `O(log(n))`.

## Method of implementation
To obtain a time complexity of `0(log(n))`, I applied a recursive function that halves the search space (of integers) 
at each time step. 
Since integers are "naturally sorted", I can treat the search space as a binary tree. 
The search space at the beginning, starts from 0 and ends at the input number. The integer in the middle of the search space is squared 
and compared to the number. If the squared is larger than the number, the search space of integers is reassigned/reduced to the 
"left side" of the middle integer - i.e., integers with smaller value than the current middle number. On the otherhand,
if the square of the middle integer is less than the input number, the search space of integers is reduced to the 
"right side" of the middle integer - i.e., integers with larger value than the current middle number. \
In the event that no square of any integer returns the input number, the search space "left bound" and "right bound" will
be recursively reduced to a single integer.
Overall, the space complexity is `O(1)` because the same variables are "reused/reassigned" at each recursive step - 
i.e., no new variables/data structure are created at each recursive step.

Time complexity = `O(log(n))` \
Space complexity = `O(1)`