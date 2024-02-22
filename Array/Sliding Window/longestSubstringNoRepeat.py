'''
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        result = 0

        l = 0
        for r in range(len(s)):
            # if we get duplicate update set
            while s[r] in charSet:
                charSet.remove(s[l]) # remove leftmost
                l += 1
            charSet.add(s[r]) # add new char of right
            result = max(result, r - l + 1) #compare current window
        return result
    
def main():
    solutionObj = Solution()
    print(solutionObj.lengthOfLongestSubstring("abcabcbb"))
if __name__ == '__main__':
    main()

# answer 3
    
    '''
        i = 0
        j = 0
        result = 0
        hashmap ={}
        
        while (j<len(s)):
            hashmap[s[j]] = 1 + hashmap.get(s[j], 0)

            
            if len(hashmap) == (j - i + 1):     # here all unique chars in window= window size
                result = max(result, j - i + 1)     # compare max and set in map
                j += 1
            #elif (len(hashmap) > j - i + 1):        # this condition won't be hit
                #j += 1
            elif (len(hashmap) < j - i + 1):        #  some characters are repeating since window size is larger than the map
                while (len(hashmap) < j - i + 1):       # when mapsize<w.s, means above
                    hashmap[s[i]] = hashmap[s[i]] - 1   #decrease the count when no of unique chars> k till it is 0
                    if hashmap[s[i]] == 0:
                        del hashmap[s[i]]
                    i += 1      # unique char till size is < k
                j += 1
        return result
'''