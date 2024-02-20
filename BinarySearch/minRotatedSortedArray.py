'''
153. Find Minimum in Rotated Sorted Array
Solved
Medium
Topics
Companies
Hint
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
'''

class Solution:
    def findMin(self, nums):
        res = nums[0]    # default value  as leftmost
        l, r = 0, len(nums) - 1

        while l <= r:       # valid position already sorted
        # if we are in left sorted part for sorted subarray
            if nums[l] < nums[r]:   
                res = min(res, nums[l])     # set leftmost value
                break
            # not sorted
            m = l + (r - l) // 2
            res = min(res, nums[m])
            # if mid is part of left sorted portion,
            # / then set l to after mid as we need to search min in right sorted portion
            if nums[m] >= nums[l]:  
                l = m + 1
            else:
                r = m - 1       # search left sorted portion otherwise
        return res
    
def main():
    solutionObj = Solution()
    print(solutionObj.findMin([4,5,6,7,0,1,2]))
if __name__ == '__main__':
    main()