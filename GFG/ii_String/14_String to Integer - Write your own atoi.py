'''
Given a string s, the task is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

Skip any leading whitespaces.
Check for a sign ('+' or '-'), default to positive if no sign is present.
Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
If the integer is greater than 231 - 1, then return 231 - 1 and if the integer is smaller than -231, then return -231.
Examples:

Input: s = "-123"
Output: -123

Input: s = " -"
Output: 0
Explanation: No digits are present, therefore 0.

Input: s = " 1231231231311133"
Output: 2147483647
Explanation: The converted number is greater than 231 - 1, therefore print 231 - 1 = 2147483647.

Input: s = "-999999999999"
Output: -2147483648
Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.

Input: s = " -0012gfg4"
Output: -12
Explanation: Nothing is read after -12 as a non-digit character 'g' was encountered.

Algorithm:

The basic idea is to follow the atoi() algorithm in order and covering all the edge cases:

Skip the leading whitespaces by iterating from the first character.
Now, check for at most one sign character ('+' or '-') and maintain a sign variable to keep track of the sign of the number.
Finally, read all the digits and construct the number until the first non-digit character is encountered or end of the input string is reached.
While constructing the number, if the number becomes greater than 231 - 1, print 231 - 1. Similarly, if the number becomes less than -231, print -231.
How to check if the number is greater than 231 - 1 or smaller than -231 ?

The naive way is to use a data type which has size greater than 32 bits like long, BigInteger to store the number. However, we can also use 32-bit integer by appending the digits one-by-one and for each digit, check if appending current digit to the number will make it underflow (< -231) or overflow(> 231- 1). While appending a digit to the current number, we can have 3 cases:

Case 1: current number < (231 - 1)/10 or current number > -231/10: Simply append the digit to the current number as it won't cause overflow/underflow.
Case 2: current number > (231 - 1)/10 or current number < -231/10: Return (231 - 1) in case of overflow and -231 in case of underflow.
Case 3: current number = (231 - 1)/10 or current number = -231/10: In this case, if current number = (231 - 1)/10, then only 0-7 digits can be appended and if current number = -231/10, then only 0-8 digits can be appended.

'''

def myAtoi(s: str) -> int:
    sign = 1
    res = 0
    idx = 0

    while idx < len(s) and s[idx] == ' ':
        idx += 1
    
    if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
        if s[idx] == '-':
            sign = -1
        idx += 1

    while idx < len(s) and '0' <= s[idx] <= '9':
        res = 10 * res + (ord(s[idx]) - ord('0'))

        if res > (2**31 - 1):
            return sign * (2**31 - 1) if sign == 1 else -2**31

        idx += 1

    return res * sign

s = "  -0012g4"
print(myAtoi(s)) 