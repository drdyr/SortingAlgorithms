import random

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

def merge_sort(arr):
    def merge(a,b): # helper function merging two different sorted arrays
        c = [] # final sorted array
        # start at beginning of both sorted arrays
        a_idx, b_idx = 0, 0

        # compare item from each list and add smaller item to merged list
        while a_idx < len(a) and b_idx < len(b):
            if a[a_idx] < b[b_idx]:
                c.append(a[a_idx])
                a_idx += 1
            else:
                c.append(b[b_idx])
                b_idx += 1

        # if a empty, add the rest of b and vice-versa
        if a_idx == len(a):
            c += b[b_idx:]
        else:
            c += a[a_idx:]
        return c

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right)


x = [random.randint(0,100) for _ in range(50)]

print(merge_sort(x))