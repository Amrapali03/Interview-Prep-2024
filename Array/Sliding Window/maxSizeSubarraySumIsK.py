'''
* Given an array arr[] of size n containing positive integers.
 * The problem is to find the length of the longest sub-array having sum equal to the given value k.
 *
 * Examples:
 * Input : arr[] = { 10, 5, 2, 7, 1, 9 },
 *         k = 15
 * Output : 4
 */

'''
class Solution:
    def maxSubArrayPositive(self, nums, k):
        i = 0
        j = 0
        newsum = 0
        res = 0
            
        while (j < len(nums)):
            newsum = newsum + nums[j]
            
            if newsum < k:     
                j += 1          # increment j to fetch the sum
            elif newsum == k:      # condition met
                window = j - i + 1
                res = max(res, window)      # compare max window size
                j += 1      # we need next candidate
            elif newsum > k:
                while (newsum > k):        # iterate till sum>k
                    newsum = newsum - nums[i] # remove from i to reduce sum
                    i += 1                 # move i
                j += 1                  # sum <5 so move j to get sum=5
        
        return res  


def main():
    solutionObj = Solution()
    print(solutionObj.maxSubArrayPositive([4,1,1,1,2,3,5], 5))

if __name__ == '__main__':
    main()

