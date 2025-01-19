'''
Given a string s, the task is to find the minimum number of characters to be added to the front of s to make it palindrome. A palindrome string is a sequence of characters that reads the same forward and backward.

Examples: 

Input: s = "abc"
Output: 2
Explanation: We can make above string palindrome as "cbabc", by adding 'b' and 'c' at front.

Input: str = "aacecaaaa"
Output: 2
Explanation: We can make above string palindrome as "aaaacecaaaa" by adding two a's at front of string.
'''

'''
The observation is that the longest palindromic prefix becomes longest palindromic suffix of its reverse.

For string = aacecaaaa
Reverse string = aaaacecaa
longest palindromic prefix = aacecaa

Now to find this prefix the idea is to use lps array of KMP algorithm, as each index of lps array represents the longest proper prefix which is also a suffix. First we concatenate the given string s with a special character '$' and with the reverse of given string s', then we will get lps array for this concatenated string( s + '$' + s').

We only need the last value of this lps[] array because it gives us the longest suffix of the reversed string that matches the prefix of the original string i.e., these many characters already satisfy the palindrome property. Finally minimum number of characters needed to make the string a palindrome is the length of the input string minus the last entry of our lps array. 
'''

# Python program for getting minimum character to be
# added at front to make string palindrome

def computeLPSArray(pat):
    n = len(pat)
    lps = [0] * n

    # lps[0] is always 0
    len_lps = 0

    # loop calculates lps[i] for i = 1 to n-1
    i = 1
    while i < n:
      
        # If the characters match, increment len
        # and set lps[i]
        if pat[i] == pat[len_lps]:
            len_lps += 1
            lps[i] = len_lps
            i += 1
        
        # If there is a mismatch
        else:
          
            # If len is not zero, update len to 
            # the last known prefix length
            if len_lps != 0:
                len_lps = lps[len_lps - 1]
                
            # No prefix matches, set lps[i] to 0
            else:
                lps[i] = 0
                i += 1
    return lps

# Method returns minimum character to be added at
# front to make string palindrome
def minChar(s):
    n = len(s)
    rev = s[::-1]

    # Get concatenation of string, special character
    # and reverse string
    s = s + "$" + rev

    # Get LPS array of this concatenated string
    lps = computeLPSArray(s)

    # By subtracting last entry of lps array from
    # string length, we will get our result
    return n - lps[-1]

if __name__ == "__main__":
    s = "AACECAAAA"
    print(minChar(s))