'''
Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge both the arrays and rearrange the elements such that the smallest n elements are in a[] and the remaining m elements are in b[]. All elements in a[] and b[] should be in sorted order.

Examples: 

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output: a[] = [2, 2, 3, 4], b[] = [7, 10] 
Explanation: Combined sorted array = [2, 2, 3, 4, 7, 10], array a[] contains smallest 4 elements: 2, 2, 3 and 4, and array b[] contains remaining 2 elements: 7, 10.

Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output: a[] = [1, 2, 3, 5, 8, 9], b[] = [10, 13, 15, 20]
Explanation: Combined sorted array = [1, 2, 3, 5, 8, 9, 10, 13, 15, 20], array a[] contains smallest 6 elements: 1, 2, 3, 5, 8 and 9, and array b[] contains remaining 4 elements: 10, 13, 15, 20.

Input: a[] = [0, 1], b[] = [2, 3]
Output: a[] = [0, 1], b[] = [2, 3] 
Explanation: Combined sorted array = [0, 1, 2, 3], array a[] contains smallest 2 elements: 0 and 1, and array b[] contains remaining 2 elements: 2 and 3.

# Python Code to Merge two sorted arrays a[] and b[] without 
# extra space using insert of insertion sort

def mergeArrays(a, b):
  
    # Traverse b[] starting from the last element
    for i in range(len(b) - 1, -1, -1):
      
        # If b[i] is smaller than the largest element of a[]
        if a[-1] > b[i]:
          
            # Place b[i] in the correct position in a[], 
            # and move last element of a[] to b[]
            last = a[-1]
            j = len(a) - 2
            while j >= 0 and a[j] > b[i]:
                a[j + 1] = a[j]
                j -= 1
            
            a[j + 1] = b[i]
            b[i] = last

if __name__ == "__main__":
    a = [1, 5, 9, 10, 15, 20]
    b = [2, 3, 8, 13]
    mergeArrays(a, b)

    for ele in a:
        print(ele, end=" ")
    print()
    for ele in b:
        print(ele, end=" ")

'''

# Python program to merge two sorted arrays a[] and b[] 
# without extra space Using swap and sort
def mergeArrays(a, b):
    i = len(a) - 1
    j = 0

    # Swap smaller elements from b[] with larger elements from a[]
    while i >= 0 and j < len(b):
        if a[i] < b[j]:
            i -= 1
        else:
            a[i], b[j] = b[j], a[i]
            i -= 1
            j += 1

    # Sort both arrays
    a.sort()
    b.sort()

if __name__ == "__main__":
    a = [1, 5, 9, 10, 15, 20]
    b = [2, 3, 8, 13]
    mergeArrays(a, b)

    for ele in a:
        print(ele, end=' ')
    print()
    for ele in b:
        print(ele, end=' ')