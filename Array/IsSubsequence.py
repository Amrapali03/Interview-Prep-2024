'''
392. Is Subsequence
Solved
Easy
Topics
Companies
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1
            j += 1
        # returns True if i has reached the length of s, indicating that all characters of s have been found
        return i == len(s)
    
def main():
    solutionObj = Solution();
    print (solutionObj.isSubsequence("abc","ahbgdc"))

if __name__ == '__main__':
    main()