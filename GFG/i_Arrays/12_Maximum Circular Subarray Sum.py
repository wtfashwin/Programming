'''
Given a circular array arr[] of size n, find the maximum possible sum of a non-empty subarray.

Examples: 

Input: arr[] = {8, -8, 9, -9, 10, -11, 12}
Output: 22
Explanation: Circular Subarray {12, 8, -8, 9, -9, 10} has the maximum sum, which is 22.

Input: arr[] = {10, -3, -4, 7, 6, 5, -4, -1}
Output: 23 
Explanation: Circular Subarray {7, 6, 5, -4, -1, 10} has the maximum sum, which is 23.

Input: arr[] = {-1, 40, -14, 7, 6, 5, -4, -1}
Output: 52
Explanation: Circular Subarray {7, 6, 5, -4, -1, -1, 40} has the maximum sum, which is 52. '''

# Python program to find maximum Subarray Sum in Circular
# subarray by considering all possible subarrays

def circularSubarraySum(arr):
    totalSum = 0    
    currMaxSum = 0
    currMinSum = 0
    maxSum = arr[0]
    minSum = arr[0]
    
    for i in range(len(arr)):
      
        # Kadane's to find maximum sum subarray
        currMaxSum = max(currMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, currMaxSum) 
        
        # Kadane's to find minimum sum subarray
        currMinSum = min(currMinSum + arr[i], arr[i])
        minSum = min(minSum, currMinSum)
        
        # Sum of all the elements of input array
        totalSum += arr[i]
    
    normalSum = maxSum
    circularSum = totalSum - minSum
    
    # If the minimum subarray is equal to total Sum
    # then we just need to return normalSum
    if minSum == totalSum:
        return normalSum
    
    return max(normalSum, circularSum)

arr = [8, -8, 9, -9, 10, -11, 12]
print(circularSubarraySum(arr))