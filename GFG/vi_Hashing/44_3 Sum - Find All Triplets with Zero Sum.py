'''
Given an array arr[], the task is to find all possible indices {i, j, k} of triplet {arr[i], arr[j], arr[k]} such that their sum is equal to zero and all indices in a triplet should be distinct (i != j, j != k, k != i). We need to return indices of a triplet in sorted order, i.e., i < j < k.

Examples :

Input: arr[] = {0, -1, 2, -3, 1}
Output: {{0, 1, 4}, {2, 3, 4}}
Explanation:  Two triplets with sum 0 are:
arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0

Input: arr[] = {1, -2, 1, 0, 5}
Output: {{0, 1, 2}}
Explanation: Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0

Input: arr[] = {2, 3, 1, 0, 5}
Output: {{}}
Explanation: There is no triplet with sum 0
'''

# Python program to find all triplets with zero sum using hashing
def findTriplets(arr):

    # Set to handle duplicates
    resSet = set()
    n = len(arr)
    mp = {}

    # Store sum of all the pairs with their indices
    for i in range(n):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if s not in mp:
                mp[s] = []
            mp[s].append((i, j))

    for i in range(n):

        # Find remaining value to get zero sum
        rem = -arr[i]
        if rem in mp:
            for p in mp[rem]:
                
                # Ensure no two indices are the same in the triplet
                if p[0] != i and p[1] != i:
                    curr = sorted([i, p[0], p[1]])
                    resSet.add(tuple(curr))

    return [list(triplet) for triplet in resSet]

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    res = findTriplets(arr)
    for triplet in res:
        print(triplet[0], triplet[1], triplet[2])