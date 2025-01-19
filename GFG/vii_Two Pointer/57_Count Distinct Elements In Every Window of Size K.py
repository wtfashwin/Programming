'''
Given an array arr[] of size n and an integer k, return the count of distinct numbers in all windows of size k. 

Examples: 

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output: [3, 4, 4, 3]
Explanation: First window is [1, 2, 1, 3], count of distinct numbers is 3.
                      Second window is [2, 1, 3, 4] count of distinct numbers is 4.
                      Third window is [1, 3, 4, 2] count of distinct numbers is 4.
                      Fourth window is [3, 4, 2, 3] count of distinct numbers is 3.

Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation: First window is [4, 1], count of distinct numbers is 2.
                      Second window is [1, 1], count of distinct numbers is 1.
'''

# Python program to count distinct elements in every window
# of size k by traversing all windows of size k

from collections import defaultdict

# Function to count distinct elements in every window of size k
def countDistinct(arr, k):
    n = len(arr)  
    res = []
    freq = defaultdict(int)
  
    # Store the frequency of elements of the first window
    for i in range(k):
        freq[arr[i]] += 1
  
    # Store the count of distinct elements of the first window
    res.append(len(freq))
  
    for i in range(k, n):
        freq[arr[i]] += 1
        freq[arr[i - k]] -= 1
      
        # If the frequency of arr[i - k] becomes 0, remove it from the hash map
        if freq[arr[i - k]] == 0:
            del freq[arr[i - k]]
      
        res.append(len(freq))
      
    return res


if __name__=='__main__':
      arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4

    res = countDistinct(arr, k)
    print(*res)