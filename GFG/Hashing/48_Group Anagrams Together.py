'''
Given an array of words arr[], the task is to groups strings that are anagrams. An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

Example:

Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.

Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"],["rat", "tar", "art"]]
Explanation:
Group 1: "abc", "bac" and "cab" are anagrams.
Group 2: "listen", "silent" and "enlist" are anagrams.
Group 3: "rat", "tar" and "art" are anagrams.
'''

# Python Code to group anagrams together by using frequency
# as keys

MAX_CHAR = 26

# function to generate hash of word s
def getHash(s):
    hashList = []
    freq = [0] * MAX_CHAR
    
    # Count frequency of each character
    for ch in s:
        freq[ord(ch) - ord('a')] += 1
    
    # Append the frequency to construct the hash
    for i in range(MAX_CHAR):
        hashList.append(str(freq[i]))
        hashList.append("$")
    
    return ''.join(hashList)

def anagrams(arr):
    res = []
    mp = {}
    
    for i in range(len(arr)):
        key = getHash(arr[i])
        
        # If key is not present in the hash map, add
        # an empty group (list) in the result and
        # store the index of the group in hash map
        if key not in mp:
            mp[key] = len(res)
            res.append([])
        
        # Insert the string in its correct group
        res[mp[key]].append(arr[i])
    
    return res

if __name__ == "__main__":
    arr = ["act", "god", "cat", "dog", "tac"]
    
    res = anagrams(arr)
    for group in res:
        for word in group:
            print(word, end=" ")
        print()