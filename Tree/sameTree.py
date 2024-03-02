'''
100. Same Tree
Solved
Easy
Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true
'''
from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

def main():
    # Create tree nodes for p
    p3 = TreeNode(3)
    p2 = TreeNode(2)
    p1 = TreeNode(1, p2, p3)

    # Create tree nodes for q
    q3 = TreeNode(3)
    q2 = TreeNode(2)
    q1 = TreeNode(1, q2, q3)

    # Create instance of Solution class
    sol = Solution()

    # Check if trees p and q are the same
    print(sol.isSameTree(p1, q1))  # Output should be True

if __name__ == "__main__":
    main()
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        deq = deque([(p, q),])

        while deq:
            p, q = deq.popleft()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            deq.append((p.left, q.left))
            deq.append((p.right, q.right))
        
        return True
'''