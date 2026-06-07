# Linear Search :

# Linear Search checks each element until the desired value is found or list ends.

# Time Complexity: O(n)

# Algorithm Steps :

# 1. Start from the first element of the array.
# 2. Compare the current element with the target value.
# 3. If both are equal, return the position/index.
# 4. Otherwise, move to the next element.
# 5. Repeat until the element is found or the array ends.
# 6. If the array ends and the element is not found, return -1.

# Key Idea : Searches elements one by one sequentially.
# It checks each element one by one from the beginning until:
# The target element is found, or
# The array ends.

# Algorithm : 
for each element in array:
    if element == target:
        return index
return -1


# Python implementation of Linear Search :
def linear_search(nums, target):
 # Loop through every element
    for i in range(len(nums)):
# Check if current element equals target
        if nums[i] == target:
            return i
# Target not found
    return -1
nums = [10, 25, 30, 45, 50]
print(linear_search(nums, 45))


# Time complexity :

# Best Case: O(1) - when the target is the first element, as there is only one comparison.
# Worst Case: O(n) - when the target is the last element or not present at all, as it requires checking every element.
# Average Case: O(n) - on average, it will check half of the elements before finding the target or concluding it's not present.