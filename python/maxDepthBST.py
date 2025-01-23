# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.height(root)
        
    def height(self, node: TreeNode)-> int:
        if node is None:
            return 0
        lHeight = self.height(node.left)
        rHeight = self.height(node.right)

        return max(lHeight, rHeight) + 1

        
        