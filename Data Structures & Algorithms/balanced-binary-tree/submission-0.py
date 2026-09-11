# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(root):
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                if abs(l - r) > 1:
                    self.res = False
                return max(l, r) + 1
            return 0
        dfs(root)
        return self.res