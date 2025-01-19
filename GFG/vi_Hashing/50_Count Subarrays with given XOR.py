'''
Given an array of integers arr[] and a number k, the task is to count the number of subarrays having XOR of their elements as k.

Examples: 

Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6].

Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9].
'''

# Python Program to count all subarrays having
# XOR of elements as given value K using Hash Map

def subarrayXor(arr, k):
    res = 0

    # Create map that stores number of prefix arrays
    # corresponding to a XOR value
    mp = {}

    prefXOR = 0

    for val in arr:
        # Find XOR of current prefix
        prefXOR ^= val

        # If prefXOR ^ k exists in mp then there is a subarray
        # ending at i with XOR equal to k
        res += mp.get(prefXOR ^ k, 0)

        # If this prefix subarray has XOR equal to k
        if prefXOR == k:
            res += 1

        # Add the XOR of this subarray to the map
        mp[prefXOR] = mp.get(prefXOR, 0) + 1

    # Return total count of subarrays having XOR of
    # elements as given value k
    return res

if __name__ == "__main__":
    arr = [4, 2, 2, 6, 4]
    k = 6

    print(subarrayXor(arr, k))