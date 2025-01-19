'''
Given an array stalls[] which denotes the position of a stall and an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

Examples: 

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: We can place cow 1 at position 1, cow 2 at position 4 and cow 3 at position 9. So, the maximum possible minimum distance between two cows is 3.

Input: stalls[] = [6, 7,  9, 11, 13, 15], k = 4
Output: 2
Explanation: We can place cow 1 at position 6, cow 2 at position 9, cow 3 at position 11 and cow 4 at position 15. So, the maximum possible minimum distance between two cows is 2.
'''

# Python program to find maximum possible minimum distance
# between any two cows using binary search

def check(stalls, k, dist):
    
    # Place first cow at 0th index
    cnt = 1  
    prev = stalls[0] 
    for i in range(1, len(stalls)):
        
        # If the current stall is at least dist away
        # from the previous one place the cow here
        if stalls[i] - prev >= dist:
            prev = stalls[i] 
            cnt += 1

    # Return true if we are able to place all 'k' cows
    return cnt >= k

def aggressiveCows(stalls, k):
    
    # sorting the array to ensure stalls in sequence
    stalls.sort()
    res = 0 

    # Search Space for Binary Search
    lo = 1
    hi = stalls[-1] - stalls[0] 

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        # If the mid distance is possible, update
        # the result and search for larger distance
        if check(stalls, k, mid):
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    
    return res

if __name__ == "__main__":
    stalls = [1, 2, 4, 8, 9] 
    k = 3
    ans = aggressiveCows(stalls, k)
    print(ans)