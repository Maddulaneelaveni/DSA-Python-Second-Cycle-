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