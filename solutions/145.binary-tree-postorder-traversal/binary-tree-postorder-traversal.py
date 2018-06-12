# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ans = []

        if root == None:
            return []

        s = []


        s.append(root)
        while s:
            node = s.pop()
            ans.append(node.val)

            if node.left != None:
                s.append(node.left)
                
            if node.right != None:
                s.append(node.right)

        ans.reverse()
    
        return ans
