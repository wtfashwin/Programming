'''Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.

Examples:

Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: arr[] = {-2, -4}
Output: -2
Explanation: The subarray {-2} has the largest sum -2.

Input: arr[] = {5, 4, 1, 7, 8}
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.'''

'''
Kadane's Algorithm - O(n) Time and O(1) Space
The idea of Kadane's algorithm is to traverse over the array from left to 
right and for each element, find the maximum sum among all subarrays ending 
at that element. The result will be the maximum of all these values.

But, the main issue is how to calculate maximum sum among all the subarrays 
ending at an element in O(1) time?

To calculate the maximum sum of subarray ending at current element, 
say maxEnding, we can use the maximum sum ending at the previous element. 
So for any element, we have two choices:

Choice 1: Extend the maximum sum subarray ending at the previous element 
by adding the current element to it. If the maximum subarray sum ending at 
the previous index is positive, then it is always better to extend the subarray.
Choice 2: Start a new subarray starting from the current element. If the 
maximum subarray sum ending at the previous index is negative, it is always 
better to start a new subarray from the current element.
This means that maxEnding at index i = max(maxEnding at index (i - 1) + arr[i], arr[i]) 
and the maximum value of maxEnding at any index will be our answer. '''

# Python Program for Maximum Subarray Sum using Kadane's Algorithm
# Function to find the maximum subarray sum
def maxSubarraySum(arr):
    
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        
        # Find the maximum sum ending at index i by either extending 
        # the maximum sum subarray ending at index i - 1 or by
        # starting a new subarray from index i
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update res if maximum subarray sum ending at index i > res
        res = max(res, maxEnding)
    
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(maxSubarraySum(arr))
