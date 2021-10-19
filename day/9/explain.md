# Part 2
## Challenges
- Refrain from reading the whole input
- The number of contiguous numbers that must be summed is not known
## High-level process
- Create 2 `while` loops:
    - The outer one goes down a line at a time `(1)`, initializes a `sum value` with the value of this line
    - The inner one increments the `sum value` by each of the following lines
        - If the sum equals to the target, return what the puzzle asks for
        - If the sum is greater than the target, break and execute the next iteration of the outer loop