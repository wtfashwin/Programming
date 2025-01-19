'''
Given an integer array arr[] of size n, find the inversion count in the array. Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Note: Inversion Count for an array indicates that how far (or close) the array is from being sorted. If the array is already sorted, then the inversion count is 0, but if the array is sorted in reverse order, the inversion count is maximum. 

Examples: 

Input: arr[] = {4, 3, 2, 1}
Output: 6

Input: arr[] = {1, 2, 3, 4, 5}
Output: 0
Explanation: There is no pair of indexes (i, j) exists in the given array such that arr[i] > arr[j] and i < j

Input: arr[] = {10, 10, 10}
Output: 0

'''

#We can use merge sort to count the inversions in an array. 
# First, we divide the array into two halves: 
# left half and right half. Next, we recursively count the 
# inversions in both halves. While merging the two halves back 
# together, we also count how many elements from the left half 
# array are greater than elements from the right half array, as 
# these represent cross inversions (i.e., element from the left 
# half of the array is greater than an element from the right half 
# during the merging process in the merge sort algorithm). 
# Finally, we sum the inversions from the left half, right half, 
# and the cross inversions to get the total number of inversions 
# in the array. This approach efficiently counts inversions while 
# sorting the array.

# Python program to Count Inversions in an array using merge sort

# This function merges two sorted subarrays arr[l..m] and arr[m+1..r] 
# and also counts inversions in the whole subarray arr[l..r]

def countAndMerge(arr, l, m, r):
  
    n1 = m - l + 1
    n2 = r - m

    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    res = 0
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += (n1 - i)
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

    return res

def countInv(arr, l, r):
    res = 0
    if l < r:
        m = (r + l) // 2

        res += countInv(arr, l, m)
        res += countInv(arr, m + 1, r)

        res += countAndMerge(arr, l, m, r)
    return res

def inversionCount(arr):
    return countInv(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(inversionCount(arr))
