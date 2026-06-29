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

# Advantages
# Very fast on average.
# Average time complexity is O(n log n).
# Widely used in practice.
# Works efficiently for large datasets.

# Disadvantages
# Worst-case time complexity is O(n²) if pivots are chosen poorly.
# Recursive implementation can lead to deep recursion in the worst case.
# The version shown here is not in-place because it creates new lists (left, middle, and right), so it uses extra memory.

# Simple Flow :
# Choose Pivot
#       ↓
# Partition into:
# Left (< Pivot)
# Pivot (= Pivot)
# Right (> Pivot)
##     ↓
# Recursively sort Left and Right
 #     ↓
# Combine:
# Sorted Left + Pivot + Sorted Right

# Algorithm Steps
# Select a Pivot element.
# Partition the array into:
# Elements smaller than Pivot
# Pivot element
# Elements greater than Pivot
# Recursively apply Quick Sort on the left partition.
# Recursively apply Quick Sort on the right partition.
# Combine the sorted left partition, Pivot, and sorted right partition.
# Continue until all partitions contain one or zero elements.


# Example Array:
# arr = [8, 3, 1, 7, 0, 10, 2]
# RECURSION TREE


 #                   [8,3,1,7,0,10,2]
 #                          7
#                 /                   \
#        [3,1,0,2]                 [8,10]
 #             0                       10
 #         /     \                  /    \
 #       []    [3,1,2]            [8]    []
 #                1
 #             /     \
 #           []     [3,2]
 #                     2
 #                  /     \
   #              []      [3]


# Code :
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Sort an array - Leetcode 912

class Solution:
    def sortArray(self, nums):
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr)//2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick_sort(left) + middle + quick_sort(right)
        return quick_sort(nums)
    
# Input:
nums = [5,2,3,1]
# Output:
[1,2,3,5]


# Top K Frequent Elements - Leetcode
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [x for x,_ in count.most_common(k)]
    



