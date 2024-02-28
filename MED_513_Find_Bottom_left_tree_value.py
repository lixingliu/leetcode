# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append(root)

        while(len(queue) > 0):
            node = queue.pop(0)

            leftmost_value = node.val

            if (node.right != None):
                queue.append(node.right)

            if (node.left != None):
                queue.append(node.left)
        return leftmost_value
            

'''
Simple if we learn level-order traversal

Simply get all the values at each level and when we reach the lowest level, pop all the rights and we will have only the left value left
'''