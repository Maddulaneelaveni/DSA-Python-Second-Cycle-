# Quick Sort :

# Quick Sort is also divide and conquer. It picks a pivot element and partitions the array into two — elements smaller than pivot and greater than pivot — then sorts them recursively.
# Time Complexity: O(n log n) average, O(n²) worst.
# It follows the divide and conquer approach.

# Definition
# Quick Sort selects one element called the pivot, places all smaller elements to its left and all larger elements to its right, then recursively sorts both parts.

# Key Idea: Partition the array around a pivot and recursively sort the left and right partitions.

# Case	       Time Complexity	     Reason

# Best Case	    O(n log n)	       Pivot divides the array into nearly equal halves at each step.
# Average Case	O(n log n)	       Random pivots usually produce reasonably balanced partitions.
# Worst Case	O(n²)	            Pivot is always the smallest or largest element, creating highly unbalanced partitions (e.g., one side has n-1 elements and the other has 0).

# Why is the average case O(n log n)?
# At each recursive level:
# Partitioning all elements takes O(n) time.
# The array is split into roughly half-sized parts.
# The number of levels is about log n.
# So: O(n) × O(log n) = O(n log n)