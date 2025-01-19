'''
Given an array arr[] consisting of only 0s, 1s, and 2s. The task is to sort the array, i.e., put all 0s first, then all 1s and all 2s in last.

This problem is the same as the famous "Dutch National Flag problem". The problem was proposed by Edsger Dijkstra. The problem is as follows:

Given n balls of colour red, white or blue arranged in a line in random order. You have to arrange all the balls such that the balls with the same colours are adjacent with the order of the balls, with the order of the colours being red, white and blue (i.e., all red coloured balls come first then the white coloured balls and then the blue coloured balls). 

Examples:

Input: arr[] = {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}
Explanation: {0, 0, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.

Input: arr[] = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
Explanation: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.
'''

def sort012(arr):
    n = len(arr)
    lo = 0
    hi = n - 1
    mid = 0

    while mid <= hi:
      if arr[mid] == 0:
        arr[lo], arr[mid] = arr[mid], arr[lo]
        lo = lo + 1
        mid = mid + 1
        
      elif arr[mid] == 1:
        mid = mid + 1
        
      else:
        arr[mid], arr[hi] = arr[hi], arr[mid]
        hi = hi - 1
        
    return arr

arr = [0, 1, 2, 0, 1, 2]
arr = sort012(arr)

for x in arr:
    print(x, end=" ")