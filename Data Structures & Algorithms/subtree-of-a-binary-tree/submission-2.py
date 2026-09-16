# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            if self.isSameTree(root, subRoot):
                return True

            return (
                self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot)
            )
        return False

    def isSameTree(self, root, subRoot):
        if root and subRoot:
            if subRoot.val == root.val:
                left = self.isSameTree(root.left, subRoot.left)
                right = self.isSameTree(root.right, subRoot.right)
                return left and right
            return False    
        if not root and not subRoot:
            return True
        return False