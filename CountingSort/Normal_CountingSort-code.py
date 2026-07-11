def counting_sort(arr):

    # Find the maximum element
    max_val = max(arr)
    # Create count array
    count = [0] * (max_val + 1)
    # Count frequency of each element
    for num in arr:
        count[num] += 1
    # Index to place sorted elements
    index = 0
    # Traverse count array
    for i in range(len(count)):
        # Place each element based on its frequency
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1
    # Return sorted array
    return arr
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))