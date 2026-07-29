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