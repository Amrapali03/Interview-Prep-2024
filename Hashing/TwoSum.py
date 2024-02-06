'''
1. Two Sum
Solved
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
class Solution:
    def twoSum(self, nums, target):
        map = dict()
        for idx, num in enumerate(nums):
            diff = target - num
            
            if diff in map:
                return [map[diff], idx]
            else:
                map[num] = idx

def main():
    solutionObj = Solution();
    print (solutionObj.twoSum([2,7,11,15],9))

if __name__ == '__main__':
    main()

'''
  d={}
  for i in range(len(input)):
    # Current value at the current index
    cur_value = input[i]
    
    # Calculate the complement needed to reach the target
    complement = target - cur_value
    
    # Check if the complement is already in the dictionary
    if complement in d:
    
        # If found, return the indices of the two elements that sum up to the target
        return [d[complement], i]
    
    # Otherwise, store the current value and its index in the dictionary
    d[cur_value] = i

# If no such pair is found, return [-1, -1]
  return [-1, -1]
'''