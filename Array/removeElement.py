class Solution:
    def removeElement(self, nums, val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i]!= val:
                # partition
                nums[k] = nums[i]
                k += 1
        return k


def main():
    solutionObj = Solution();
    print(solutionObj.removeElement([3,2,2,3], 3))
    
if __name__ == '__main__':
    main()

# 2