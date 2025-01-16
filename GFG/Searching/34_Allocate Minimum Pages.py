'''
Given an array arr[] and an integer k, where arr[i] denotes the number of pages of a book and k denotes total number of students. All the books need to be allocated to k students in contiguous manner, with each student getting at least one book.

The task is to minimize the maximum number of pages allocated to a student. If it is not possible to allocate books to all students, return -1.

Examples:

Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Books can be distributed in following ways:

[12] and [34, 67, 90] - The maximum pages assigned to a student is 34 + 67 + 90 = 191.
[12, 34] and [67, 90] - The maximum pages assigned to a student is 67 + 90 = 157.
[12, 34, 67] and [90] - The maximum pages assigned to a student is 12 + 34 + 67 = 113.
The third combination has the minimum pages assigned to a student which is 113.

Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.

Input: arr[] = [22, 23, 67], k = 1 

'''

# Python program to find the minimum page limit by iterating
# over all possible page limits

# Function to check if books can be allocated to
# all k students without exceeding 'pageLimit'
def check(arr, k, pageLimit):
    
    # Starting from the first student
    cnt = 1
    pageSum = 0
    for pages in arr:
        
        # If adding the current book exceeds the page 
        # limit, assign the book to the next student
        if pageSum + pages > pageLimit:
            cnt += 1
            pageSum = pages
        else:
            pageSum += pages
            
    # If books can assigned to less than k students then
    # it can be assigned to exactly k students as well
    return cnt <= k

def findPages(arr, k):
    
    # If number of students are more than total books
    # then allocation is not possible
    if k > len(arr):
        return -1
    
    # Search space for Binary Search
    lo = max(arr)
    hi = sum(arr)
    res = -1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if check(arr, k, mid):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
            
    return res

if __name__ == "__main__":
    arr = [12, 34, 67, 90]
    k = 2
    print(findPages(arr, k))