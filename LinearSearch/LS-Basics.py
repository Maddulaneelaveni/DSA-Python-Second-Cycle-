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

# Output: 3 (since 45 is at index 3 in the array)

# Example:

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
arr = [5, 3, 2, 8, 1]
key = 2
result = linear_search(arr, key)
if result != -1:
    print(f"Element found at index: {result}")  
else:
    print("Element not found in the array.")    
# Output: Element found at index: 2 (since 2 is at index 2 in the array)

# Time complexity :

# Best Case: O(1) - when the target is the first element, as there is only one comparison.
# Worst Case: O(n) - when the target is the last element or not present at all, as it requires checking every element.
# Average Case: O(n) - on average, it will check half of the elements before finding the target or concluding it's not present.

# Space Complexity: O(1) - No extra space is used, as the search is performed in-place without any additional data structures.


# Advantages:
# Easy to understand, Works on unsorted arrays, No preprocessing needed, Simple implementation

# Disadvantages:
# Inefficient for large datasets, Time-consuming, Not suitable for sorted arrays, High time complexity, Checks every element, Not efficient compared to Binary Search

# Common Patterns include :
# 1. Finding the first occurrence of a target value in an array.
# 2. Finding the last occurrence of a target value in an array.
# 3. Counting the number of occurrences of a target value in an array.
# 4. Finding the maximum or minimum value in an array.
# 5.Finding an element
# 6.Checking existence
