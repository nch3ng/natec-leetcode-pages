# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# all values are distinguished

class Solution:
    def isValidBST(self, root):
        return self.isValidBSTwithBoundary(root, None, None)
    
    def isValidBSTwithBoundary(self, root, leftbound, rightbound):
        if root == None:
            return True

        if (leftbound != None and leftbound.val >= root.val) or (rightbound != None and rightbound.val <= root.val):
            return False
    
        return self.isValidBSTwithBoundary(root.left, leftbound, root) and self.isValidBSTwithBoundary(root.right, root, rightbound)
    
            