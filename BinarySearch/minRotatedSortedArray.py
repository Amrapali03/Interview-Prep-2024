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