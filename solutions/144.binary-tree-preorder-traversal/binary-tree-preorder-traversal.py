from collections import deque
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        q = deque()
        if root == None:
            return []
        
        q.append(root)

        while q:
            node = q.popleft()
            ans.append(node.val)

            if node.left != None:
                ans += self.preorderTraversal(node.left)
            
            if node.right != None:
                ans += self.preorderTraversal(node.right)

        return ans