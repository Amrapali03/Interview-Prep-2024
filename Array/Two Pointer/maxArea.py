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

def main():
    solutionObj = Solution()
    print(solutionObj.maxArea([1,8,6,2,5,4,8,3,7]))

if __name__ == '__main__':
    main()