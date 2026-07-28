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

# Daily Temperatures
# Algorithm: Monotonic Decreasing Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def daily_temperatures(temperatures):
    n = len(temperatures)
    # Result array initialized with 0.
    # If no warmer day exists, the answer remains 0.
    result = [0] * n
    # Stack stores the INDICES of temperatures.
    stack = []
    # Traverse each temperature
    for i in range(n):
        # If the current temperature is warmer than the temperature
        # at the index on the top of the stack,
        # we have found the next warmer day.
        while stack and temperatures[i] > temperatures[stack[-1]]:
            # Remove the previous day's index
            prev_index = stack.pop()
            # Calculate the number of days waited
            result[prev_index] = i - prev_index
        # Push the current day's index onto the stack
        stack.append(i)
    # Any indices left in the stack do not have a warmer day.
    # Their values remain 0.
    return result
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer = daily_temperatures(temperatures)
print("Temperatures:", temperatures)
print("Answer      :", answer)


# Interview Points :
# Pattern: Monotonic Decreasing Stack
# Store: Indices (not temperatures)
# Why indices? To calculate the number of days (i - prev).
# Pop condition:
# temperatures[i] > temperatures[stack[-1]]
# Answer after popping:
# ans[prev] = i - prev