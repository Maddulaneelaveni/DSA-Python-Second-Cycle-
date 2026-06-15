# What is Bubble Sort?
# Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
# The largest element moves to the end after each pass, just like a bubble rising to the surface.

# Time Complexity: O(n²)

# Algorithm Steps :

#Start from the first element.
#Compare two adjacent elements.
#If the first element is greater than the second element, swap them.
#Move to the next pair of adjacent elements.
#Continue until the end of the array.
#After the first pass, the largest element reaches its correct position.
#Repeat the process for the remaining unsorted elements.
#Stop when all elements are sorted.

#Key Idea: The largest element "bubbles up" to the end after every pass.

# Example : [5, 3, 8, 4, 2]
# Pass 1: 5 3 8 4 2 → 3 5 4 2 8
# Pass 2: 3 5 4 2 8 → 3 4 2 5 8
# Pass 3: 3 4 2 5 8 → 3 2 4 5 8
# Pass 4: 3 2 4 5 8 → 2 3 4 5 8


# Code :
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

