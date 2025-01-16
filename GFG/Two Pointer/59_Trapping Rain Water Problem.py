'''Trapping Rainwater Problem states that given an array of n non-negative integers arr[] representing an elevation map where the width of each bar is 1, compute how much water it can trap after rain.

Examples:  
Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
Output: 10
Explanation: The expected rainwater to be trapped is shown in the above image.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides

Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
Output: 9
Explanation : We trap 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units of water.

'''

def maxWater(arr):
    left = 1
    right = len(arr) - 2

    # lMax : Maximum in subarray arr[0..left-1]
    # rMax : Maximum in subarray arr[right+1..n-1]
    lMax = arr[left - 1]
    rMax = arr[right + 1]

    res = 0
    while left <= right:
      
        # If rMax is smaller, then we can decide the 
        # amount of water for arr[right]
        if rMax <= lMax:
          
            # Add the water for arr[right]
            res += max(0, rMax - arr[right])

            # Update right max
            rMax = max(rMax, arr[right])

            # Update right pointer as we have decided 
            # the amount of water for this
            right -= 1
        else: 
          
            # Add the water for arr[left]
            res += max(0, lMax - arr[left])

            # Update left max
            lMax = max(lMax, arr[left])

            # Update left pointer as we have decided 
            # the amount of water for this
            left += 1
    return res

if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(maxWater(arr))