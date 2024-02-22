'''
424. Longest Repeating Character Replacement
Solved
Medium
Topics
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
'''
'''
424. Longest Repeating Character Replacement
Solved
Medium
Topics
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
'''

class Solution:
    def characterReplacement(self, s, k):
        l = 0
        res = 0
        count = {} # count occurences of each char

        for r in range(len(s)):
            # increment count
            count[s[r]] = 1 + count.get(s[r],0)
            # current window is valid
            # len window - count of most frequent char, size 26 is max
            while (r - l + 1) -max(count.values()) > k:
                # count of char in left decrement
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

def main():
    solutionObj = Solution()
    print(solutionObj.characterReplacement("AABABBA", 1))
if __name__ == '__main__':
    main()

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
        '''