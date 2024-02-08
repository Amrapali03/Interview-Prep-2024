'''

167. Two Sum II - Input Array Is Sorted
Solved
Medium
Topics
Companies
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''
class Solution:
    def twoSumII(self, numbers, target):
        l=0
        r = len(numbers) -1

        while l<r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r-=1
            elif curSum < target:
                l+=1
            else:
                return [l+1, r+1] # rememeber to give +1 as we start from 1 not 0 as index
            
def main():
    solutionObj = Solution()
    print(solutionObj.twoSumII([2,7,11,15], 9))

if __name__ == '__main__':
    main()