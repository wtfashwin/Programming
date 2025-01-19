'''
Largest subarray of 0's and 1's
Given an array arr of 0s and 1s. Find and return the 
length of the longest subarray with equal number of 0s and 1s.
Examples:

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.
Input: arr[] = [0]
Output: 0
Explnation: There is no subarray with an equal number of 0s and 1s.

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 1
'''

class Solution:
    def maxLen(self, arr):
        n = len(arr)
        s = [0] * len(arr)

        if (arr[0] == 0):
            s[0] = -1
        else:
            s[0] = 1
        for i in range(1, len(s)):

            if (arr[i] == 0):
                s[i] = s[i - 1] - 1
            else:
                s[i] = s[i - 1] + 1

        d = dict()

        mx_len = 0

        i = 0

        for j in s:

            if (j == 0):
                mx_len = max(mx_len, i + 1)

            if (d.get(j) != None):
                mx_len = max(mx_len, i - d[j])

            else:
                d[j] = i

            i = i + 1

        return mx_len
