'''
Given a sorted matrix mat[][] of size nxm and an element x, the task is to find if x is present in the matrix or not. Matrix is sorted in a way such that all elements in a row are sorted in increasing order and for row i, where 1 <= i <= n-1, the first element of row i is greater than or equal to the last element of row i-1.

Examples:

Input: x = 14, mat[][] = [[ 1, 5, 9],
[14, 20, 21],
[30, 34, 43]]
Output: true

Input: x = 42, mat[][] = [[ 1, 5, 9, 11],
[14, 20, 21, 26],
[30, 34, 43, 50]]
Output: false
'''

# Python program to search in the sorted matrix using
# binary search

# Function to search for x in the matrix using binary search
def searchMatrix(mat, x):
    n = len(mat)
    m = len(mat[0])

    lo, hi = 0, n * m - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        # Find row and column of element at mid index
        row = mid // m
        col = mid % m

        # If x is found, return true
        if mat[row][col] == x:
            return True

        # If x is greater than mat[row][col], search in
        # right half
        if mat[row][col] < x:
            lo = mid + 1

        # If x is less than mat[row][col], search in
        # left half
        else:
            hi = mid - 1

    return False

if __name__ == "__main__":
    mat = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
    x = 14

    if searchMatrix(mat, x):
        print("true")
    else:
        print("false")