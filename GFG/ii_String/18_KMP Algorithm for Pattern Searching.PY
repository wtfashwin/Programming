'''
Given two strings txt and pat, the task is to return all indices of occurrences of pat within txt.

Examples:

Input: txt = "abcab", pat = "ab"
Output: [0, 3]
Explanation: The string "ab" occurs twice in txt, first occurrence starts from index 0 and second from index 3.

Input: txt=  "aabaacaadaabaaba", pat =  "aaba"
Output: [0, 9, 12]
Explanation:

LPS Array
LPS is the Longest Proper Prefix which is also a Suffix. A proper prefix is a prefix that doesn't include whole string. For example, prefixes of "abc" are "", "a", "ab" and "abc" but proper prefixes are "", "a" and "ab" only. Suffixes of the string are "", "c", "bc", and "abc".
Each value, lps[i] is the length of longest proper prefix of pat[0..i] which is also a suffix of pat[0..i].
Construction of LPS Array
lps[0] is always 0 since a string of length one has no non-empty proper prefix. We store the value of the previous LPS in a variable len, initialized to 0. As we traverse the pattern, we compare the current character at index i, with the character at index len.

Case 1 - pat[i] = pat[len]: this means that we can simply extend the LPS at the previous index, so increment len by 1 and store its value at lps[i].

Case 2 - pat[i] != pat[len] and len = 0: it means that there were no matching characters earlier and the current characters are also not matching, so lps[i] = 0.

Case 3 - pat[i] != pat[len] and len > 0: it means that we can't extend the LPS at index i-1. However, there may be a smaller prefix that matches the suffix ending at i. To find this, we look for a smaller suffix of pat[i-len...i-1] that is also a proper prefix of pat. We then attempt to match pat[i] with the next character of this prefix. If there is a match, pat[i] = length of that matching prefix. Since lps[i-1] equals len, we know that pat[0...len-1] is the same as pat[i-len...i-1]. Thus, rather than searching through pat[i-len...i-1], we can use lps[len - 1] to update len, since that part of the pattern has already been matched.

'''
# Python program to search the pattern in given text 
# using KMP Algorithm

def constructLps(pat, lps):
    
    # len stores the length of longest prefix which 
    # is also a suffix for the previous index
    len_ = 0
    m = len(pat)
    
    # lps[0] is always 0
    lps[0] = 0

    i = 1
    while i < m:
        
        # If characters match, increment the size of lps
        if pat[i] == pat[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        
        # If there is a mismatch
        else:
            if len_ != 0:
                
                # Update len to the previous lps value 
                # to avoid redundant comparisons
                len_ = lps[len_ - 1]
            else:
                
                # If no matching prefix found, set lps[i] to 0
                lps[i] = 0
                i += 1

def search(pat, txt):
    n = len(txt)
    m = len(pat)

    lps = [0] * m
    res = []

    constructLps(pat, lps)

    # Pointers i and j, for traversing 
    # the text and pattern
    i = 0
    j = 0

    while i < n:
        
        # If characters match, move both pointers forward
        if txt[i] == pat[j]:
            i += 1
            j += 1

            # If the entire pattern is matched 
            # store the start index in result
            if j == m:
                res.append(i - j)
                
                # Use LPS of previous index to 
                # skip unnecessary comparisons
                j = lps[j - 1]
        
        # If there is a mismatch
        else:
            
            # Use lps value of previous index
            # to avoid redundant comparisons
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res 

if __name__ == "__main__":
    txt = "aabaacaadaabaaba"
    pat = "aaba"

    res = search(pat, txt)
    for i in range(len(res)):
        print(res[i], end=" ")