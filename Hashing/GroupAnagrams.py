'''
49. Group Anagrams
Solved
Medium
Topics
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # do not take sort as it will belong m.n logn
        # mapping charcount to list of anagrams
        res = defaultdict(list)

        for s in strs:
            count  = [0] * 26 # we have a....z

            for c in s:
                # map a to 0 and z to index 25
                count[ord(c) - ord("a")] +=1
            # we change dict to defaultdict for key not present
            # list cannot be keys

            # group all anagrams with same count
            res[tuple(count)].append(s)
        return res.values()



        