def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current position has the minimum
        min_index = i
        for j in range(i + 1, n):
            # Find index of the minimum element
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the current position
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
arr = list(map(int, input("Enter numbers separated by space: ").split()))
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
