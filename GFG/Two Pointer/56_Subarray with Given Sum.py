'''
Given a 1-based indexing array arr[] of non-negative integers and an integer sum. You mainly need to return the left and right indexes(1-based indexing) of that subarray. In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

Examples: 

Input: arr[] = [15, 2, 4, 8, 9, 5, 10, 23], target = 23
Output: [2, 5]
Explanation: Sum of subarray arr[2...5] is 2 + 4 + 8 + 9 = 23.

Input: arr[] = [1, 10, 4, 0, 3, 5], target = 7
Output: [3, 5]
Explanation: Sum of subarray arr[3...5] is 4 + 0 + 3 = 7.

Input: arr[] = [1, 4], target = 0
Output: [-1]
Explanation: There is no subarray with 0 sum.
'''

# Function to find a continuous sub-array which adds up to
# a given number.
def subarraySum(arr, target):
    res = []
    n = len(arr)

    # Pick a starting point for a subarray
    for s in range(n):
        curr = 0

        # Consider all ending points
        # for the picked starting point
        for e in range(s, n):
            curr += arr[e]
            if curr == target:
                res.append(s + 1)
                res.append(e + 1)
                return res

    # If no subarray is found
    return [-1]
      
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    target = 23
    res = subarraySum(arr, target)

    for ele in res:
        print(ele, end=" ")