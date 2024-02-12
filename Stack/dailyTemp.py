'''
739. Daily Temperatures
Solved
Medium
Topics
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
'''
class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0]* len(temperatures)
        stack= [] # pair[temp, index]

        for day_index, curr_temp in enumerate(temperatures):
            # if stack empty then if this temp> top of stack
            while stack and curr_temp >  stack[-1][0]:
                stack_temp, stack_index = stack.pop() 
                # no of days to find warmer temp
                res[stack_index] = day_index - stack_index
            stack.append([curr_temp, day_index])
        return res

def main():
    solutionObj = Solution()
    print(solutionObj.dailyTemperatures([73,74,75,71,69,72,76,73]))

if __name__ == '__main__':
    main()



'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer

'''
