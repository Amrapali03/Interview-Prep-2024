class Solution:
    def maximumSumSubarray(self, arr, k):

        i = 0
        j = 0
        csum = 0
        maximum = 0
        while j < len(arr):
            csum = csum + arr[j]
            if (j - i + 1) < k:
                j += 1
            elif (j - i + 1) == k:
                maximum = max(csum, maximum)
                csum = csum - arr[i]
                j += 1
                i += 1
        return maximum
    
def main():
    solutionObj = Solution()
    print(solutionObj.maximumSumSubarray([2,5,1,8,2,9,1], 3))
if __name__ == '__main__':
    main()

# 19


