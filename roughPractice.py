'''

# valid parenthesis
class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        left_list = ["(", "{", "["]
        right_list = [")", "}", "]"]
        for i in s:
            if i in left_list:
                stack.append(i)
            elif i in right_list:
                closing = right_list.index(i)
                if len(stack) == 0 or (left_list[closing] != stack[len(stack)-1]):
                    return False
                else:
                    stack.pop()
            if len(stack)==0:
                return True
            else:
                return False
                

def main():
    solutionObj = Solution()
    print(solutionObj.isValid("()[]{}"))

if __name__ == '__main__':
    main()
    '''

Me = {'Masters':'Business Analytics', 'Open for':'Full-time (Aug\'24)', 'Skills':'Excel, SQL, Python, Power Bi, Tableau, ML', 'Roles':'Data Analyst, Business Analyst, Data Scientist, Product/Program Manager'}
print(Me)