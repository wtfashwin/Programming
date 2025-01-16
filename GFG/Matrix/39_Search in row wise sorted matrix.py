'''
Given a row-wise sorted matrix mat[][] and an integer x, the task is to check if x is present in mat[][] or not. Note that there is no ordering among column elements.

Examples:

Input: x = 9, mat[][] = [[3, 4, 9],
[2, 5, 6],
[9, 25, 27]]
Output: true
Explanation: mat[0][2] is equal to 9.

Input: x = 56, mat[][] = [[19, 22, 27, 38, 55, 67]]
Output: false
Explanation: 56 is not present in mat[][].

'''

# Python program to search an element in row-wise
# sorted matrix 

def search(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        
        # If x == mid, return true
        if x == arr[mid]:
            return True
        
        # If x < arr[mid], search in the left half
        if x < arr[mid]:
            hi = mid - 1
        
        # If x > arr[mid], search in the right half
        else:
            lo = mid + 1
    return False


def searchRowMatrix(mat, x):
    n, m = len(mat), len(mat[0])
    
    # Iterate over all the rows to find x
    for i in range(n):
        
        # Perform binary search on the ith row
        if search(mat[i], x):
            return True
    
    # If x was not found, return false
    return False

if __name__ == "__main__":
    mat = [[3, 4, 9],
           [2, 5, 6],
           [9, 25, 27]]
    x = 9
    if searchRowMatrix(mat, x):
        print("true")
    else:
        print("false")
