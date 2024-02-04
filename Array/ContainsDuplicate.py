'''
Question: 

'''

class Solution:
    def containsDuplicate(self, nums):
        dic1 ={}
        for i in nums:
            if i in dic1:
                return True
            else:
                 dic1[i] = 1
        return False
    
def main():
    solutionObj = Solution();

    print (solutionObj.containsDuplicate([1,8,6,8]))
    print (solutionObj)

if __name__ == '__main__':
    main()