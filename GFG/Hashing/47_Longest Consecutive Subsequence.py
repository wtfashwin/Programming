'''
Given an array of integers, the task is to find the length of the longest subsequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order. 

Examples:  

Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are from 1 to 6. These 6 numbers form the longest consecutive subsequence [2, 6, 1, 4, 5, 3].

Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: The subsequence [1, 3, 4, 2] is the longest subsequence of consecutive elements

Input: arr[] = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
Output: 5
Explanation: The subsequence [36, 35, 33, 34, 32] is the longest subsequence of consecutive elements.
'''

# Python program to find longest consecutive subsequence

def longestConsecutive(arr):
    st = set()
    res = 0

    # Hash all the array elements
    for val in arr:
        st.add(val)

    # Check each possible sequence from the start 
    # then update length
    for val in arr:

        # If current element is the starting element of a sequence
        if val in st and (val - 1) not in st:

            # Then check for next elements in the sequence
            cur = val
            cnt = 0
            while cur in st:

                # Remove this number to avoid recomputation
                st.remove(cur)
                cur += 1
                cnt += 1

            # Update optimal length
            res = max(res, cnt)

    return res


if __name__ == "__main__":
    arr = [2, 6, 1, 9, 4, 5, 3]
    print(longestConsecutive(arr))