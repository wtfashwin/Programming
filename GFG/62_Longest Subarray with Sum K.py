'''
Given an array arr[] containing integers and an integer k, 
your task is to find the length of the longest subarray where 
the sum of its elements is equal to the given value k. 
If there is no subarray with sum equal to k, return 0.

Examples:
Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = 15 is [-5, 8, -14, 2, 4] of length 5.

Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].

Constraints:
1 ≤ arr.size() ≤ 105
-104 ≤ arr[i] ≤ 104
-109 ≤ k ≤ 109

'''
#Prefix sum

class Solution:
    def longestSubarray(self, arr, k):  
        prefix_sum_map = {}
        prefix_sum_map[0] = -1
        total = 0
        n = len(arr)
        a = 0
        
        for i in range(n):
            total += arr[i]
            
            if (total - k) in prefix_sum_map:
                a = max(a , i - prefix_sum_map[total-k])
                
            if total not in prefix_sum_map:
                prefix_sum_map[total] = i
                
        return a


if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")