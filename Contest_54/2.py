"""
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: 
            "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Input: "10101"
Output: 4
Explanation: There are 4 substrings: 
"10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
"""

s="1000001"

def char_count(s,i):
    if i<=len(s)-1:
        bar=1
        while(i<len(s)-1 and s[i+1]==s[i]):
            bar+=1
            i+=1
        return bar, i+1
    else:
        return 0, i+1
def countBinarySubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    total=0
    then = 0
    if len(s)==1:
        return 0
    while(i<len(s)):
        i=i-then
        (now,i)=char_count(s,i)
        (then,i)=char_count(s,i)
        total+=min(now,then)     
    return total

print countBinarySubstrings(s)
