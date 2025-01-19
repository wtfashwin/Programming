'''Given an array arr[] of size n, the task is to print the lexicographically next greater permutation of the given array. If there does not exist any greater permutation, then find the lexicographically smallest permutation of the given array.

Let us understand the problem better by writing all permutations of [1, 2, 4] in lexicographical order

[1, 2, 4], [1, 4, 2], [2, 1, 4], [2, 4, 1], [4, 1, 2] and [4, 2, 1]

If we give any of the above (except the last) as input, we need to find the next one in sequence. If we give last as input, we need to return the first one.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is 2 4 5 0 1 7

Input: arr = {3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation. So, the next permutation is the lowest one.

Iterate over the given array from end and find the first index (pivot) which doesn't follow property of non-increasing suffix, (i.e,  arr[i] < arr[i + 1]).
If pivot index does not exist, then the given sequence in the array is the largest as possible. So, reverse the complete array. For example, for [3, 2, 1], the output would be [1, 2, 3]
Otherwise, Iterate the array from the end and find for the successor (rightmost greater element) of pivot in suffix.
Swap the pivot and successor
Minimize the suffix part by reversing the array from pivot + 1 till n.'''

# Python Program to find the next permutation by 
# generating only next

def next_permutation(arr):
    n = len(arr)
    
    # Find the pivot index
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    
    # If pivot point does not exist, 
    # reverse the whole array
    if pivot == -1:
        arr.reverse()
        return

    # Find the element from the right 
    # that is greater than pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Reverse the elements from pivot + 1 to the end in place
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


arr = [ 2, 4, 1, 7, 5, 0 ]
next_permutation(arr)
print(" ".join(map(str, arr)))