# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None:
            return []
        def helper(root, result):
            if root.left != None:
                helper(root.left, result)
            result.append(root.val)
            if root.right != None:
                helper(root.right, result)
            return
        helper(root, result)
        return result
    

            
        