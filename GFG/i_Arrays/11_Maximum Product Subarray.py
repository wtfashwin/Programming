'''Given an integer array, the task is to find the maximum product of any subarray.

Examples:

Input: arr[] = {-2, 6, -3, -10, 0, 2}
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180

Input: arr[] = {-1, -3, -10, 0, 60}
Output: 60
Explanation: The subarray with maximum product is {60}. '''

'''
traversing in both directions - O(n) Time and O(1) Space
We will follow a simple approach that is to traverse from the start and keep track of the running product and if the running product is greater than the max product, then we update the max product. Also, if we encounter '0' then make product of all elements till now equal to 1 because from the next element, we will start a new subarray.

But what is the problem with this approach?

Problem will occur when our array will contain odd no. of negative elements. In that case, we have to reject one negative element so that we can even no. of negative elements and their product can be positive. Now, since subarray should be contiguous so we can't simply reject any one negative element. We have to either reject the first negative element or the last negative element.

Now, if we traverse from start then only the last negative element can be rejected and if we traverse from the last then the first negative element can be rejected. So we will traverse from both ends and find the maximum product subarray. 

Complexity Analysis:

Time Complexity: O(n), where n is the size of input array.
Auxiliary Space: O(1)'''

# Python program to find Maximum Product Subarray using 
# Traversal From Starting and End of an Array

# function to find the product of max product subarray
def maxProduct(arr):
    n = len(arr)
    maxProd = float('-inf')
  
    # leftToRight to store product from left to Right
    leftToRight = 1
  
    # rightToLeft to store product from right to left
    rightToLeft = 1
  
    for i in range(n):
        if leftToRight == 0:
            leftToRight = 1
        if rightToLeft == 0:
            rightToLeft = 1
      
        # calculate product from index left to right
        leftToRight *= arr[i]
      
        # calculate product from index right to left
        j = n - i - 1
        rightToLeft *= arr[j]
        maxProd = max(leftToRight, rightToLeft, maxProd)
    
    return maxProd

arr = [-2, 6, -3, -10, 0, 2]
print(maxProduct(arr))

