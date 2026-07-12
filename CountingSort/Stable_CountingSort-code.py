def stable_counting_sort(arr):
    # Find the maximum element
    max_val = max(arr)
    # Create count array
    count = [0] * (max_val + 1)
    # Count frequency of each element
    for num in arr:
        count[num] += 1
    # Convert frequency to cumulative (prefix sum)
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # Create output array
    output = [0] * len(arr)
    # Traverse from right to left for stability
    for i in range(len(arr) - 1, -1, -1):
        # Place element at its correct position
        output[count[arr[i]] - 1] = arr[i]
        # Decrease count for the next occurrence
        count[arr[i]] -= 1
    # Return stable sorted array
    return output
arr = [4, 2, 2, 8, 3, 3, 1]
print(stable_counting_sort(arr))

# Difference
# Normal Counting Sort
# Counts frequencies.
# Directly writes sorted values back.
# Not stable.

# Stable Counting Sort
# Counts frequencies.
# Converts frequencies to prefix sums (cumulative counts).
# Traverses the original array from right to left.
# Places elements in an output array.
# Stable, so it preserves the relative order of equal elements. This is why Radix Sort uses Stable Counting Sort.