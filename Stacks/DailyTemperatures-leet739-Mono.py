# LeetCode 739. Daily Temperatures

# Approach: Monotonic Decreasing Stack (Indices)
# Idea :
# Store indices in the stack, not temperatures.
# The stack keeps temperatures in decreasing order.
# If today's temperature is greater than the temperature at the stack's top index:
# We've found the next warmer day.
# The answer is:
# current_index - previous_index
# Push the current day's index onto the stack.

# Time Complexity
# O(n) - Every index is pushed once and popped once.
# Space Complexity
# O(n) - Stack + answer array.