'''
155. Min Stack
Medium
10.3K
694
company
Amazon
company
Bloomberg
company
Expedia
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []  # it will always have the current minimum
        

    def push(self, val):
        self.stack.append(val)      # value is always appended in first stack
        if not self.minStack or val <= self.minStack[-1]:   # when minstack is empty or if it has value greater than current val , then we need to append current smaller value to minstack
            self.minStack.append(val)
    
    def pop(self) -> None:

        # if self.minStack[-1] == self.stack[-1]: # when the new value in stack is same as value in minstack we pop from minstack
        self.minStack.pop()
        self.stack.pop()        # we continue popping from original stack always
        

    def top(self) -> int:
        return self.stack[-1]       # no edge cases, as this will be called when a stack is non empty

    def getMin(self) -> int:
        return self.minStack[-1]        # it is called when stack is non empty, top of minstack is called
        


# Your MinStack object will be instantiated and called as such:
def main():
    obj = MinStack()
    obj.push([-2])
    obj.push([-3])
    obj.push([0])
    param_4 = obj.getMin()
    print(param_4)
    param_3 = obj.pop()
    print(param_3)
    param_2 = obj.getMin()
    print(param_2)
# answer -3, None, [-2]
if __name__ == '__main__':
    main()


# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]