'''
14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs):
        result = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result

def main():
    solutionObj = Solution();
    print (solutionObj.longestCommonPrefix(["flower","flow","flight"]))

if __name__ == '__main__':
    main()

