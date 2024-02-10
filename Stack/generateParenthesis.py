
'''
22. Generate Parentheses
Solved
Medium
Topics
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
'''
# Brute Force
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(p_string):
            left_count = 0
            for p in p_string:
                if p == '(':
                    left_count += 1
                else:
                    left_count -= 1
                if left_count < 0:
                    return False
            return left_count == 0
        
        answer = []
        queue = collections.deque([""])
        while queue:
            cur_string = queue.popleft()

            if len(cur_string) == 2 * n:
                if isValid(cur_string):
                    answer.append(cur_string)
                continue
            queue.append(cur_string + ")")
            queue.append(cur_string + "(")
        return answer

'''
class Solution:
    def generateParenthesis(self, n):
        # stack is global, so we need to add everytime by popping after we finish backtrack
        stack = []
        res = []
        # no need to pass stack, res, n in backtrack as it is nested
        def backtrack(openN, closedN):
            # base case, always needs to be returned
            if openN == closedN == n:
                # join all char in stack to empty string, then append to res
                res.append( "".join(stack))
                return
            
            # condition of adding open bracket
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0,0)
        return res
    
def main():
    solutionObj = Solution()
    print(solutionObj.generateParenthesis(3))

if __name__ == '__main__':
    main()