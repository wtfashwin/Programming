'''
Given a sorted array of distinct positive integers arr[] and integer k, the task is to find the kth positive number that is missing from arr[].

Examples : 

Input: arr[] = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: Missing are 1, 5, 6, 8, 9, 10, ... and 5th missing number is 9.

Input: arr[] = [1, 2, 3], k = 2
Output: 5
Explanation: Missing are 4, 5, 6.... and 2nd missing number is 5.

Input: arr[] = [3, 5, 9, 10, 11, 12], k = 2
Output: 2
Explanation: Missing are 1, 2, 4, 6, 7, 8, 13,... and 2nd missing number is 2.
'''

# Python Program to find Kth missing positive number
# using Binary Search

# Function to find the k-th missing positive number
def kthMissing(arr, k):
    lo = 0
    hi = len(arr) - 1
    res = len(arr) + k

    # Binary Search for index where arr[i] > (i + k)
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] > mid + k:
            res = mid + k
            hi = mid - 1
        else:
            lo = mid + 1

    return res

if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(kthMissing(arr, k))