'''
Given an unsorted array of positive integers, the task is to find the number of triangles that can be formed with three different array elements as three sides of triangles.

For a triangle to be possible from 3 values as sides, the sum of the two values (or sides) must always be greater than the third value (or third side). 

Examples: 

Input: arr[] = [4, 6, 3, 7]
Output: 3
Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. 
Note that [3, 4, 7] is not a possible triangle.  

Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
Output: 6
Explanation: There can be 6 possible triangles:
[10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300]

Input: arr[] = [1, 2, 3]
Output: 0
Examples: No triangles are possible.
'''

# Python code to count the number of possible triangles
# using Two Pointers Technique

def countTriangles(arr):
    res = 0
    arr.sort()

    # Iterate through the array, fixing the largest side at arr[i]
    for i in range(2, len(arr)):
      
        # Initialize pointers for the two smaller sides
        left, right = 0, i - 1

        while left < right:
            if arr[left] + arr[right] > arr[i]:
                # arr[left] + arr[right] satisfies the triangle inequality,
                # so all pairs (x, right) with (left <= x < right) are valid
                res += right - left

                # Move the right pointer to check smaller pairs
                right -= 1
                
            else:
                # Move the left pointer to increase the sum
                left += 1

    return res


if __name__ == "__main__":
    arr = [4, 6, 3, 7]
    print(countTriangles(arr))