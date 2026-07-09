def stable_counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    # Step 1: Count frequency
    for num in arr:
        count[num] += 1
    # Step 2: Prefix Sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    # Step 3: Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output
arr = [4, 2, 2, 8, 3, 3, 1]
print(stable_counting_sort(arr))