# LeetCode 209 – Minimum Size Subarray Sum
# Problem Statement :
# Given an array of positive integers nums and an integer target, return the minimum length of a contiguous subarray whose sum is greater than or equal to target.
# If no such subarray exists, return 0.

# Example
# Input:
# target = 7
# nums = [2,3,1,2,4,3]

# Output:
# 2

# Explanation:
# Subarray [4,3] has sum = 7
# Length = 2 (minimum)

# Sliding Window Idea :

# Since all numbers are positive:
# Expand the window by moving right.
# Keep adding elements to window_sum.
# Once window_sum >= target,
# Update the minimum length.
# Shrink the window from the left to see if we can still satisfy the condition with a smaller window.


# Code :

def min_subarray_length(nums, target):
    left = 0
    window_sum = 0
    min_len = float("inf")
    for right in range(len(nums)):
        # Expand window
        window_sum += nums[right]
        # Shrink window while condition is satisfied
        while window_sum >= target:
            # Update answer
            min_len = min(min_len, right - left + 1)
            # Remove left element
            window_sum -= nums[left]
            left += 1
    if min_len == float("inf"):
        return 0
    return min_len
# Example
nums = [2,3,1,2,4,3]
target = 7
print(min_subarray_length(nums, target))