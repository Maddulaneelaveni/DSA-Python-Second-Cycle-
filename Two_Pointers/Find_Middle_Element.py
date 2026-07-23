# 5. Fast and Slow Pointer
# Find Middle Element

def middle_index(nums):
    slow = 0
    fast = 0
    while fast < len(nums) - 1:
        slow += 1
        fast += 2
    return nums[slow]
print(middle_index([10, 20, 30, 40, 50]))
