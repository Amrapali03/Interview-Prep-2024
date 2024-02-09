class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

def main():
    solutionObj = Solution()
    print(solutionObj.isValid("()[]{}"))

if __name__ == '__main__':
    main()

'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque() # stack from collections
        for i in s:
            if i in '{([': # 1 case: if i is "([{"
                stack.append(i) 
            else: #2 case if i not in "([{"
                if not stack: # when s like ")[]" 
                    return False 
                l = stack.pop()
                comb = l+i
                if comb != "[]" and comb != "{}" and comb != "()":
                    return False
        return not stack
'''
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # define the list
        closeToopen = {")":"(", "}": "{", "]":"["}

        for c in s:
            if c in closeToopen:    # if string exists in the map
                if stack and stack[-1] == closeToopen[c]:   # if stack exists, toplast=matching
                    stack.pop()
                else:
                    return False    # if stack has only ending brackets
            else:
                stack.append(c)
        return True if not stack else False     # as popping stack will be empty so True   

'''
'''
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

'''