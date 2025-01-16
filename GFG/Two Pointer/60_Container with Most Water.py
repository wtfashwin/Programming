'''
Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

Examples :  

Input: arr[] = [1, 5, 4, 3]
Output: 6
Explanation: 5 and 3 are 2 distance apart. So the size of the base = 2. Height of container = min(5, 3) = 3. So total area = 3 * 2 = 6.

Input: arr[] = [3, 1, 2, 4, 5]
Output: 12
Explanation: 5 and 3 are distance 4 apart. So the size of the base = 4. Height of container = min(5, 3) = 3. So total area = 4 * 3 = 12.

Input: arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
Output: 25
Explanation: 8 and 5 are 5 distance apart. So the size of the base = 5. Height of container = min(8, 5) = 5. So, total area = 5 * 5 = 12.
'''

# Python Program to find the maximum amount of water in the 
# container using Two Pointer Technique

def maxWater(arr):
    left = 0
    right = len(arr) - 1
    res = 0
    while left < right:
        
        # Find the water stored in the container between 
        # arr[left] and arr[right]
        water = min(arr[left], arr[right]) * (right - left)
        res = max(res, water)
        
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return res

  
if __name__ == "__main__":
    arr = [2, 1, 8, 6, 4, 6, 5, 5]
    print(maxWater(arr))