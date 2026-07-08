def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    # Count frequency
    for num in arr:
        count[num] += 1
    index = 0
    # Place elements back into array
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1
    return arr
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))

# Output : [1, 2, 2, 3, 3, 4, 8]