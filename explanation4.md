# Problem 4: Dutch National Flag Problem
by Cephas Tan Li-Jie
## Assignment description
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: `O(n)` does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

## Method of implementation
Since there are only 3 element types in the array, the middle valued element (1) is tracked
throughout the entire algorithm. All 0s will be "thrown" to before the 1s, and all 2s to after the 1st.
Three tracking variables are used:
1) `left_idx` - tracks the location of the first 1s.
2) `right_idx` - tracks the location before the first 2s and points at the last element not yet encountered by the `scanning_idx`.
3) `scanning_idx` - traverse the array and monitors the location of elements to be checked.

There are 3+1 possible outcome during the array traversal:
1. If a 0 is encountered, the elements of the `left_idx` and the `scanning_idx` are swapped before the `scanning_idx`
moves to the next element.
2. If a 1 is encountered, nothing happens and the scanning_idx moves to the next element.\

3. If a 2 is encountered, the elements of the `scanning_idx` and the `right_idx` are swapped before moving 
the `right_idx` by -1.

4. Finally, the last possible outcome is when the `scanning_idx` reaches the `right_idx`. Since the `right_idx` also indicates
the location of the last element of the array not yet compared and assign, a final identification and reassignment of this 
"final" element is performed before ending the traversal.

Overall, all elements are "looked at" and compared once. Therefore, the time complexity is `O(n)`.
This is also an inplace sorting algorithm. Hence, the space complexity is `0(1)`.

Time complexity = `O(n)`\
Space complexity = `O(1)`

