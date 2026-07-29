# LeetCode 496. Next Greater Element I

# Pattern- Monotonic Decreasing Stack + Hash Map

# Approach :
# Traverse nums2 from left to right.
# Maintain a monotonic decreasing stack.
# The stack stores elements whose next greater element hasn't been found yet.
# If the current element is greater than the top of the stack:
# Pop the smaller element.
# Store the current element as its next greater element in a dictionary.
# Push the current element onto the stack.
# After traversing nums2, the remaining elements in the stack have no greater element, so map them to -1.
# Traverse nums1 and use the dictionary to build the answer.

# Idea:
# Instead of searching to the right for every element (which takes O(n²)), process nums2 only once.
# The stack keeps track of elements waiting for their next greater element. As soon as a larger element appears, it becomes the answer for all smaller elements on top of the stack.
# Finally, use a hash map to answer each query from nums1 in O(1) time.

# Next Greater Element I
# Algorithm: Monotonic Decreasing Stack
# Time Complexity: O(n + m)
# Space Complexity: O(n)

def next_greater_element(nums1, nums2):

    # Stack stores elements whose next greater element
    # has not been found yet.
    stack = []

    # Dictionary stores:
    # element -> next greater element
    next_greater = {}

    # Traverse nums2
    for num in nums2:

        # Current element is the next greater element
        # for all smaller elements on the top of the stack
        while stack and num > stack[-1]:

            smaller = stack.pop()
            next_greater[smaller] = num

        # Push current element
        stack.append(num)

    # Remaining elements have no greater element
    while stack:
        next_greater[stack.pop()] = -1

    # Build answer for nums1
    result = []

    for num in nums1:
        result.append(next_greater[num])

    return result

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
answer = next_greater_element(nums1, nums2)

print("nums1 :", nums1)
print("nums2 :", nums2)
print("Answer:", answer)