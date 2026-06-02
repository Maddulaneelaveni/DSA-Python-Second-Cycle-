# Insertion sort part-1 -- HAckerank
# What is Insertion Sort?
# Insertion Sort builds the sorted array one element at a time by repeatedly taking the next unsorted element and inserting it into the correct position in the already sorted portion of the array.
# Time Complexity: O(n²)
# Algorithm Steps :
# Start from the second element (index 1) and compare it with the elements before it.
# If the current element is smaller than the previous elements, shift the larger elements one position to the right.
# Insert the current element into its correct position in the sorted portion of the array.
# Repeat the process for all elements until the entire array is sorted.
# Key Idea: The current element is compared with the sorted portion of the array and inserted into its correct position.
# Example : [5, 3, 8, 4, 2]
# Pass 1: 5 3 8 4 2 → 3 5 8 4 2