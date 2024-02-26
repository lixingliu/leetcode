# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if (p is None and q is not None):
            return False
        if p is not None and q is None:
            return False
        if (p is None and q is None):
            return True
        
        if (p.val == q.val):
            if not self.isSameTree(p.left, q.left):
                return False
            return self.isSameTree(p.right, q.right)


'''

    It can be rewritten to be shorter but the efficiency is there
    The logic behind this was constantly check the left until it hits None and 
    then check the right.

    this is done using preorder traversal

'''