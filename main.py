def quicksort(arr):
    # base case for recursion
    if len(arr) <= 1:
        return arr
    # pick arbitrary value for pivot
    pivot = arr[0]
    lower = []
    higher = []
    middle = []
    # iterate through list, add item to respective list
    for item in arr:
        if item > pivot:
            higher.append(item)
        if item < pivot:
            lower.append(item)
        else:
            middle.append(item)
    # recursion and list concatenation
    return quicksort(lower) + middle + quicksort(higher)


def selection_sort(arr):
    # iterate through array
    for i in range(len(arr)):
        min_index = i
        # find index of minimum element from index i+1 onwards
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap start of subarray with minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


