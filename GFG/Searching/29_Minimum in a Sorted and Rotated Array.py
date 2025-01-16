'''
Given a sorted array of distinct elements arr[] of size n that is rotated at some unknown point, the task is to find the minimum element in it. 

Examples: 

Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element present in the array.

Input: arr[] = [3, 1, 2]
Output: 1
Explanation: 1 is the minimum element present in the array.

Input: arr[] = [4, 2, 3]
Output: 2
Explanation: 2 is the only minimum element in the array.
'''

# Python program to find minimum element in a 
# sorted and rotated array using binary search

def findMin(arr):
    lo, hi = 0, len(arr) - 1

    while lo < hi:
      
        # The current subarray is already sorted, 
        # the minimum is at the low index
        if arr[lo] < arr[hi]:
            return arr[lo]
           
        # We reach here when we have at least
        # two elements and the current subarray
        # is rotated
      
        mid = (lo + hi) // 2

        # The right half is not sorted. So 
        # the minimum element must be in the
        # right half.
        if arr[mid] > arr[hi]:
            lo = mid + 1
          
        # The right half is sorted. Note that in 
        # this case, we do not change high to mid - 1
        # but keep it to mid. As the mid element
        # itself can be the smallest
        else:
            hi = mid

    return arr[lo]

if __name__ == "__main__":
    arr = [5, 6, 1, 2, 3, 4]
    print(findMin(arr))
