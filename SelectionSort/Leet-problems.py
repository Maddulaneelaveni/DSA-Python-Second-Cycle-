# LeetCode 1051 - Height Checker :

# Problem :
# You are given an array heights.
# Return the number of indices where:
# heights[i] is different from the position it would have in sorted order.

class Solution:
    def heightChecker(self, heights):
        expected=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
# Function Call
obj=Solution()
heights=[1, 1, 4, 2, 1, 3]
print(obj.heightChecker(heights))

# Time Complexity: O(n log n) because of the sorting step, where n is the number of elements in the heights array. The rest of the operations (comparing the original and sorted arrays) take O(n) time.