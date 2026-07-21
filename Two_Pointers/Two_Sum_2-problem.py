# 2. Opposite Direction
# Two Sum II (Sorted Array)

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []
print(two_sum([2, 7, 11, 15], 9))