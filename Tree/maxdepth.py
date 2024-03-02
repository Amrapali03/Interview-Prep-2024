'''
104. Maximum Depth of Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
'''
   
from collections import deque 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''
# recursion solution

def maxDepth(root):
    if root is None:
        return 0
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
'''
'''
# ITERATIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
'''
# BFS solution
def maxDepth(root):
    if not root:
        return 0
    level = 0
    q = deque([root])

    while q:
        for i in range(len(q)): #len at a time
            q.popleft() # pop a node and add a children if non empty
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
  
        level += 1
    return level



if __name__ == "__main__":
    # implement the tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(6)
    root.right.left.left = Node(5)
    print(root)
    print("Max Depth")
    print(maxDepth(root))