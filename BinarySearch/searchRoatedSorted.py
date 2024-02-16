'''
33. Search in Rotated Sorted Array
Solved
Medium
Topics
Companies
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

'''
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) //2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:     # left part is ascending sorted
                if target  > nums[mid]: # right of left part
                    l = mid + 1
                elif target < nums[l]: # less than mid but also less than leftmost value search right portion
                    l = mid + 1
                # OR if target > nums[mid] or target < nums[l]:
                else: # means target is less than mid but greater than left, search left so update right pointer
                    r = mid - 1

            # right sorted portion
            else:  # target less than mid and greater than left
                # OR if target < nums[mid] or target > nums[r]:
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:  # target is greater than rightmost value,we search left portion, upfdate right pointer
                    r = mid - 1
                else:
                    l = mid + 1 # target is greater than mid and less than right value, serach only right portion, update left pointer

        return -1
    
def main():
    solutionObj = Solution()
    print(solutionObj.search([4,5,6,7,0,1,2], 0))

if __name__ == '__main__':
    main()

