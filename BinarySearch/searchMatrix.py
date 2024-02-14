'''
74. Search a 2D Matrix
Solved
Medium
Topics
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
class Solution:
    def searchMatrix(self,matrix, target):
        # first we search the row to target
        rows, cols = len(matrix), len(matrix[0]) #dimension
        # first binary search
        top = 0
        bottom = rows - 1
        while top <= bottom:
            row = (top + bottom)// 2 # mid row
            if target > matrix[row][-1]: # last value
                top = row + 1 
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break # found in current row
        
        #none contained target value
        if not (top <= bottom):
            return False
    # second binary search
        row = (top + bottom) //2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


def main():
    solutionObj = Solution()
    print(solutionObj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 23))
if __name__ == '__main__':
    main()

