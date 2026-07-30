# Maximum Sum of Subarray of Size K (Fixed Sliding Window)
# Problem Statement

# Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

# Example
# Input:
# nums = [2, 1, 5, 1, 3, 2]
# k = 3

# Output:
# 9

# Explanation:
# Subarrays of size 3:
# [2,1,5] -> 8
# [1,5,1] -> 7
# [5,1,3] -> 9   ← Maximum
# [1,3,2] -> 6


# Code :

def maximum_sum_subarray(nums, k):
    n = len(nums)
    # Sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    # Slide the window
    for i in range(k, n):
        window_sum += nums[i]
        window_sum -= nums[i - k]

        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum
# Example
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(maximum_sum_subarray(nums, k))

# Complexity
# Time: O(n)
# Space: O(1)
# This is fixed-size sliding window pattern