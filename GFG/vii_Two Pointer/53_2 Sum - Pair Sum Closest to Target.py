'''
Given an array arr[] of n integers and an integer target, the task is to find a pair in arr[] such that it’s sum is closest to target.

Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

Examples:

Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: Out of all the pairs, [22, 30] has sum = 25 which is closest to 25.

Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence,[2, 7] has maximum absolute difference and closest to target.

Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.'''

# Python Program to find pair with sum closest to target 
# using Two Pointer Technique

# function to return the pair with sum closest to target
def sumClosest(arr, target):
    n = len(arr)
    arr.sort()
    res = []
    minDiff = float('inf')

    left = 0
    right = n - 1

    while left < right:
        currSum = arr[left] + arr[right]

        # Check if this pair is closer than the closest
        # pair so far
        if abs(target - currSum) < minDiff:
            minDiff = abs(target - currSum)
            res = [arr[left], arr[right]]

        # If this pair has less sum, move to greater values
        if currSum < target:
            left += 1

        # If this pair has more sum, move to smaller values
        elif currSum > target:
            right -= 1

        # If this pair has sum = target, return it
        else:
            return res

    return res

if __name__ == "__main__":
    arr = [5, 2, 7, 1, 4]
    target = 10

    res = sumClosest(arr, target)
    if len(res) > 0:
        print(res[0], res[1])