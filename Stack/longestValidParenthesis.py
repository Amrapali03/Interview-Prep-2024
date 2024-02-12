'''
32. Longest Valid Parentheses
Solved
Hard
Topics
Companies
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
'''

class Solution:
    def longestValidParentheses(self, s):
        stack =[]
        longest = 0
        n = len(s)

        stack.append(-1 )#initial
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1]) # get length
        return longest      
    
def main():
    solutionObj = Solution()
    print(solutionObj.longestValidParentheses("(()"))
    print(solutionObj.longestValidParentheses(")()())"))
if __name__ == '__main__':
    main()