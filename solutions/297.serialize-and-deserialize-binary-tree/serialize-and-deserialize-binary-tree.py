from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
          return []
        
        if not root.left and not root.right:
          return [root.val]

        ans = []
        stack = deque()
        
        node = root
        stack.append(node)
        while stack:
          node = stack.popleft()
          if node:
            ans.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
          else:
            ans.append(None)

        # trim the end
        while ans[-1] == None:
          ans.pop()

        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = None

        if not data:
          return root

        node_queue = deque()
        list = deque(data)
        val = list.popleft()
        
        if val != None:
          root = TreeNode(val)

        node_queue.append(root)
        print(node_queue)
        while list:
          t = node_queue.popleft() # start with root
          left = list.popleft()
          if list:
            right = list.popleft()
          else:
            right = None


          if left != None:
            t.left = TreeNode(left)
            node_queue.append(t.left)

          if right != None:
            t.right = TreeNode(right)
            node_queue.append(t.right)
          
        return root
