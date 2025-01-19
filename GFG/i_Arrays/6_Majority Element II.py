''' Given an array arr[] consisting of n integers, the task is to find all the array elements which occurs more than floor(n/3) times.
Note: The returned array of majority elements should be sorted.

Examples:

Input: arr[] = {2, 2, 3, 1, 3, 2, 1, 1}
Output: {1, 2}
Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3 = 2).

Input: arr[] = {-5, 3, -5}
Output: {-5}
Explanation: The frequency of -5 is 2, which is more than floor n/3 (3/3 = 1).

Input: arr[] = {3, 2, 2, 4, 1, 4}
Output: { }
Explanation: There is no majority element. 

The idea is based on the observation that there can be at most two majority elements, which appear more than n/3 times. so we can use Boyer-Moore’s Voting algorithm. As we iterate the array, We identify potential majority elements by keeping track of two candidates and their respective counts.

Steps:

Initialize two variables ele1 = -1 and ele2 = -1, for candidates and two variables cnt1 = 0 and cnt2 = 0, for counting.
In each iteration,
If an element is equal to any candidate, update that candidate's count.
If count of a candidate reaches zero then replace that candidate with current element.
If neither candidate matches and both counts are non zero, decrement the counts.
After this, in second pass we check if the chosen candidates appear more than n/3 times in the array. If they do then include them in result array.
Since any element than appears more than floor(n/3) times, will dominate over elements that appear less frequently. Whenever we encounter a different element, we decrement the count of both the candidates. This maintains at most two candidates in the array.
'''

# Python program for finding the majority element in 
# an array using Moore’s Voting algorithm

def findMajority(arr):
    n = len(arr)

    # Initialize two candidates and their counts
    ele1, ele2 = -1, -1
    cnt1, cnt2 = 0, 0

    for ele in arr:
        # Increment count for candidate 1
        if ele1 == ele:
            cnt1 += 1
        # Increment count for candidate 2
        elif ele2 == ele:
            cnt2 += 1
        # New candidate 1 if count is zero
        elif cnt1 == 0:
            ele1 = ele
            cnt1 += 1
        # New candidate 2 if count is zero
        elif cnt2 == 0:
            ele2 = ele
            cnt2 += 1
        # Decrease counts if neither candidate
        else:
            cnt1 -= 1
            cnt2 -= 1

    res = []
    cnt1, cnt2 = 0, 0

    # Count the occurrences of candidates
    for ele in arr:
        if ele1 == ele:
            cnt1 += 1
        if ele2 == ele:
            cnt2 += 1

    # Add to result if they are majority elements
    if cnt1 > n / 3:
        res.append(ele1)
    if cnt2 > n / 3 and ele1 != ele2:
        res.append(ele2)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end=" ")
