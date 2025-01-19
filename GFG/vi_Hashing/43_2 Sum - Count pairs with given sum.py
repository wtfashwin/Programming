'''
Given an array arr[] of n integers and a target value, the task is to find the number of pairs of integers in the array whose sum is equal to target.

Examples:  

Input: arr[] = {1, 5, 7, -1, 5}, target = 6
Output:  3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         

Input: arr[] = {1, 1, 1, 1}, target = 2
Output:  6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) and (1, 1).

Input: arr[] = {10, 12, 10, 15, -1}, target = 125
Output:  0
'''

# Python Program to count pairs with given sum
# using Dictionary

# Returns number of pairs in arr[0...n-1] with sum 
# equal to 'target'
def countPairs(arr, target):
    freq = {}
    cnt = 0

    for i in range(len(arr)):
        
        # Check if the complement (target - arr[i])
        # exists in the map. If yes, increment count
        if (target - arr[i]) in freq:
            cnt += freq[target - arr[i]] 
        
        # Increment the frequency of arr[i]
        freq[arr[i]] = freq.get(arr[i], 0) + 1 
    return cnt

if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5] 
    target = 6 
    print(countPairs(arr, target))