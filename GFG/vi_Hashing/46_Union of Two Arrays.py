'''
Given two arrays a[] and b[], the task is to return union of both the arrays in any order.

Note: Union of two arrays is an array having all distinct elements that are present in either array.

Examples:

Input : a[] = {1, 2, 3, 2, 1}, b[] = {3, 2, 2, 3, 3, 2}
Output : {3, 2, 1}
Explanation: 3, 2 and 1 are the distinct elements present in either array.

Input : a[] = {1, 2, 3}, b[] = {4, 5, 6}
Output : {1, 2, 3, 4, 5, 6}
Explanation: 1, 2, 3, 4, 5 and 6 are the elements present in either array.
'''

# Python program to find union of two arrays

def findUnion(a, b):
    st = set()  
    
    # Put all elements of a[] in st
    for i in range(len(a)):
        st.add(a[i])
    
    # Put all elements of b[] in st
    for i in range(len(b)):
        st.add(b[i])
    
    res = []                            

    # iterate through the set 
    # to fill the result array 
    for it in st:
        res.append(it)
    
    return res

if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    res = findUnion(a, b)

    for i in range(len(res)):
        print(res[i], end = ' ')