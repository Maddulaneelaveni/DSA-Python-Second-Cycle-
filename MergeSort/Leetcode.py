# 1. 912- Leetcode Problem- Sort an Array

# You are given an unsorted array.
# nums = [5, 2, 3, 1]
# You need to sort it in ascending order.
# Expected output: [1, 2, 3, 5]

# Constraints
# You cannot simply use sort().
# Interviewers expect you to implement a sorting algorithm.
# Merge Sort is one of the best solutions because it runs in O(n log n).

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
nums = [5, 2, 3, 1]
sorted_nums = merge_sort(nums)
print("Sorted Array:", sorted_nums)

# Output: Sorted Array: [1, 2, 3, 5]

# Time Complexity: O(n log n) because the array is divided into halves (log n) and each half is merged (n).