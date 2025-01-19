'''

Given an unsorted array of integers, the task is to find the number of subarrays having a sum exactly equal to a given number k.

Examples: 

Input : arr[] = [10, 2, -2, -20, 10], k = -10
Output : 3
Explanation: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum equal to -10.

Input : arr[] = [9, 4, 20, 3, 10, 5], k = 33
Output : 2
Explanation: Subarrays: arr[0...2], arr[2...4] have sum equal to 33.

Input : arr[] = [1, 3, 5], k = 2
Output : 0
Explanation: No subarrays with 0 sum.
'''

# Python program to count subarrays having sum K
# using Hash Map

def countSubarrays(arr, k):
    # Dictionary to store prefix sums frequencies
    prefixSums = {}
    res = 0
    currSum = 0

    for val in arr:
        # Add current element to sum so far
        currSum += val

        # If currSum is equal to desired sum, then a new subarray is found
        if currSum == k:
            res += 1

        # Check if the difference exists in the prefixSums dictionary
        if currSum - k in prefixSums:
            res += prefixSums[currSum - k]

        # Add currSum to the dictionary of prefix sums
        prefixSums[currSum] = prefixSums.get(currSum, 0) + 1

    return res

if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    k = -10
    print(countSubarrays(arr, k))