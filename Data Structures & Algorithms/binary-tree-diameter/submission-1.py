# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(root):
            if root:
                d_l = dfs(root.left)
                d_r = dfs(root.right)
                self.diameter = max(self.diameter, d_l + d_r)
                return max(d_l, d_r) + 1
            return 0
        dfs(root)
        return self.diameter