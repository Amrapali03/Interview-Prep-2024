'''
242. Valid Anagram
Solved
Easy
Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''
class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        # how to make solution with O(1) memory
# we can sort and check at beginning, we think it doesn't take extra space
        
        return sorted(s) == sorted(t)
        # memory efficient cheating solution
        # Counter(s) == Counter(t) 
        # below is for O(s*t)
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            # build hasmap
            # we increment the key, 
            # but can get error we can get if that key is not there
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # iterate hashmap
        # if char doesn't exist use get
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        return True
    
def main():
    solutionObj = Solution();
    print (solutionObj.isAnagram("anagram", "nagaram"))

if __name__ == '__main__':
    main()