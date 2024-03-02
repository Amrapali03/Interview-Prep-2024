from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubTree(self, s, t):
        if not t: # null subtree t is a sibtree of another null subtree s, leaf node
            return True
        if not s: #not necessary to write not s and not t as above first check is done
            return False
        
        if self.isSameTree(s, t):
            return True
        
        # t is equivaent to left or right subtree of s
        return (self.isSubTree(s.left, t) or self.isSubTree(s.right, t))


    def isSameTree(self, s, t) -> bool:
        # p and q are both None
        if not s and not t:
            return True
        # if both non-empty
        if not s and t and s.val == t.val:
            # if both subtrees are same
            return (self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right))
        # if one empty and one non-empty
        return False

def main():
    # Create tree nodes for s
    s4 = TreeNode(4)
    s5 = TreeNode(5)
    s2 = TreeNode(2, s4, s5)
    s3 = TreeNode(3)
    s1 = TreeNode(1, s2, s3)

    # Create tree nodes for t
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t2 = TreeNode(2, t4, t5)
    t1 = TreeNode(1, t2)

    # Create instance of Solution class
    sol = Solution()

    # Check if t is a subtree of s
    print(sol.isSubTree(s1, t1))  # Output should be True

if __name__ == "__main__":
    main()