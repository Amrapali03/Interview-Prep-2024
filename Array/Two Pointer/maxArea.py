'''
11. Container With Most Water
Solved
Medium
Topics
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
class Solution:
    def maxArea(self, height):
        res = 0
        l = 0
        r = len(height) - 1
        while l< r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l+=1 
            else:
                r-=1
        return res


def main():
    solutionObj = Solution()
    print(solutionObj.maxArea([1,8,6,2,5,4,8,3,7]))

if __name__ == '__main__':
    main()
'''
class Solution:
    def maxArea(self, height):
        left = 0
        max_area = -1
        right = len(height) - 1
        # two pointer approach till the pointers overlap
        while left < right:                                     
            temp_height = min(height[left], height[right])      # we cannot slant even if we get bigger height
            length = right - left # width
            area = length * temp_height
            
            max_area = max(max_area, area) # compare max area and area calculated to return result
            if height[right] > height[left]: # build own condition # my length will always reduce so we focus on keeping max height while looping
                left += 1  # we need to iterate left pointer to +1 as we are keeping the max height on right
            else: 
                right -= 1
                
        return max_area
'''