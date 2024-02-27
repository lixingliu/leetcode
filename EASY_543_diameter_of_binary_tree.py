# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepest(self, root, diameters):
        left = 0
        right = 0
        if (root.left is not None):
            diameters, left = self.deepest(root.left, diameters)
        if (root.right is not None):
            diameters, right = self.deepest(root.right, diameters)
        diameters.append(left + right)
        return diameters, max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        results, num = self.deepest(root, [])
        return(max(results))
        

'''
Problem was harder than listed
For each parent, you need to check how deep left and right it is
with that, you would pass all the longest diameter back to the root
and the root will determine what is the longest path

'''