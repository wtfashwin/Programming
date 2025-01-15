''' 
Given an array arr[] of size n, the task is to return an equilibrium index (if any) or -1 if no equilibrium index exists. The equilibrium index of an array is an index such that the sum of all elements at lower indexes equals the sum of all elements at higher indexes.

Note: When the index is at the start of the array, the left sum is 0, and when it's at the end, the right sum is 0.

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 0 + 3 = 3.

Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.

Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.
'''

'''
# Python program to find equilibrium index of an array
# Using nested loop

def findEquilibrium(arr):
    
    # Check for indexes one by one until
    # an equilibrium index is found 
    for i in range(len(arr)):
        # Get left sum
        leftSum = sum(arr[:i])

        # Get right sum
        rightSum = sum(arr[i + 1:])

        # If leftsum and rightsum are same, then 
        # index i is an equilibrium index
        if leftSum == rightSum:
            return i

    # If equilibrium index doesn't exist
    return -1
  
if __name__ == '__main__':
    arr = [-7, 1, 5, 2, -4, 3, 0]

    print(findEquilibrium(arr))
'''



'''
# Python program to find equilibrium index of an array
# using prefix sum and suffix sum arrays

def findEquilibrium(arr):
    n = len(arr)

    pref = [0] * n
    suff = [0] * n

    # Initialize the ends of prefix and suffix array
    pref[0] = arr[0]
    suff[n - 1] = arr[n - 1]

    # Calculate prefix sum for all indices
    for i in range(1, n):
        pref[i] = pref[i - 1] + arr[i]

    # Calculating suffix sum for all indices
    for i in range(n - 2, -1, -1):
        suff[i] = suff[i + 1] + arr[i]

    # Checking if prefix sum is equal to suffix sum
    for i in range(n):
        if pref[i] == suff[i]:
            return i

    # if equilibrium index doesn't exist
    return -1
  
if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]

    print(findEquilibrium(arr))
    '''

'''
Expected Approach:

# Python program to find equilibrium index of an array
# using prefix sum and suffix sum variables

def equilibriumPoint(arr):
    prefSum = 0
    total = sum(arr)

    # Iterate pivot over all the elements of the array
    for pivot in range(len(arr)):
        suffSum = total - prefSum - arr[pivot]
        if prefSum == suffSum:
            return pivot
        prefSum += arr[pivot]

    # There is no equilibrium point
    return -1

if __name__ == "__main__":
    arr = [1, 7, 3, 6, 5, 6]

    result = equilibriumPoint(arr)
    print(result)

'''