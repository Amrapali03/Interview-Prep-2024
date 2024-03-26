'''
58. Length of Last Word
Solved
Easy
Topics
Companies
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # no blank and no trailing spaces
        p = len(s) - 1
        while p >= 0 and s[p] == ' ':
            p -= 1

        length = 0
        while p>= 0 and s[p]!= ' ':
            p-=1
            length +=1
        return length
    
def main():
    solutionObj = Solution();
    print (solutionObj.lengthOfLastWord("Hello World"))

if __name__ == '__main__':
    main()