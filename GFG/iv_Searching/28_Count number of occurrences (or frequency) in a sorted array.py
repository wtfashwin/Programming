'''
Given a sorted array arr[] and an integer target, the task is to find the number of occurrences of target in given array.

Examples:

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: 2 occurs 4 times in the given array.

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: 4 is not present in the given array.

'''

# Python program to count occurrence of a given target
# using binary search

from bisect import bisect_left, bisect_right

# Function to find the occurrence of the given target 
# using binary search
def countFreq(arr, target):
    l = bisect_left(arr, target)
    r = bisect_right(arr, target)
    
    # Return the difference between upper bound and 
    # lower bound of the target
    return r - l

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 2
    print(countFreq(arr, target))