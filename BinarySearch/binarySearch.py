'''
704. Binary Search
Solved
Easy
Topics
Companies
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''
class Solution:
    def binarySearch(self, nums, target):
        low = 0
        mid_index = 0
        high = len(nums) -1

        while low <= high:
            mid_index = (low + high)//2
            mid_num = nums [mid_index] 

            if mid_num == target:
                return mid_index   
            elif mid_num < target:
                low = mid_index + 1
            else:
                high = mid_index - 1
        return -1



def main():
    solutionObj = Solution()
    print(solutionObj.binarySearch([-1,0,3,5,9,12], 9))

if __name__ == '__main__':
    main()

'''
left_index = 0
        right_index = len(nums) - 1
        mid_index = 0

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            mid_number = nums[mid_index]

            if mid_number == target:
                return mid_index

            if mid_number < target:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
'''