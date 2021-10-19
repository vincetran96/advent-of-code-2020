# Part 2
## Challenges
- Refrain from reading the whole input
- The number of contiguous numbers that must be summed is not known
## High-level process
- Create 2 `while` loops:
    - The outer one goes down a line at a time , initializes a single-element list with the value of this line `(1)`
    - The inner one adds the value of each of the following lines to the list in `(1)`
        - If the sum of the list equals to the target, return what the puzzle asks for
        - If the sum of the list is greater than the target, break and execute the next iteration of the outer loop