'''
Given two arrays a[] and b[], the task is find intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements and the result should contain items in any order.

Input: a[] = {1, 2, 1, 3, 1}, b[] = {3, 1, 3, 4, 1}
Output: {1, 3}
Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements

Input: a[] = {1, 1, 1}, b[] = {1, 1, 1, 1, 1}
Output: {1}
Explanation: 1 is the only common element present in both the arrays.

Input: a[] = {1, 2, 3}, b[] = {4, 5, 6}
Output: {}
Explanation: No common element in both the arrays.
'''

# Function to find intersection of two arrays
def intersection(a, b):
  
    # Put all elements of a[] in sa
    sa = set(a)

    res = []

    # Traverse through b[]
    for elem in b:
      
        # If the element is in sa
        if elem in sa:
            res.append(elem)  # Add it to the result array
            sa.remove(elem)   # Erase it from sa to avoid duplicates

    return res

# Driver code
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

res = intersection(a, b)
print(" ".join(map(str, res)))
