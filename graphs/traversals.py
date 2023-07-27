class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return arr
            node = stack.pop()
            arr.append(node.val)
            root = node.right

    def inorderTraversalRecursive(self, root):
      res = []
      self.inorderTraversalHelper(root,res)
      return res
    

    def inorderTraversalHelper(self, root, res):
      if root:
          self.inorderTraversalHelper(root.left, res)
          res.append(root.val)
          self.inorderTraversalHelper(root.right, res)

    def inorderTraversalUsingFlag(self, root):
      res = []
      stack = [(root, False)]
      while stack:
        node, visited = stack.pop()
        if node:
          if visited:
            res.append(node.val)
          else:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))
      return res

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def preorderTraversalRecursive(self, root):
        res = []
        self.preorderTraversalHelper(root, res)
        return root

    def preorderTraversalHelper(self, root, res):
        if root:
          res.append(root.val)
          self.preorderTraversalHelper(root.left, res)
          self.preorderTraversalHelper(root.right, res)

    def preorderTraversalUsingFlag(self, root):
      res = []
      stack =[(root, False)]
      while stack:
        node, visited = stack.pop()
        if node:
          if visited:
            res.append(node.val)
          else:
            stack.append((node.right, False))
            stack.append((node.left, False))
            stack.append((node, True))
        return res

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
          return
        res = []
        stack = [root]
        while stack:
          cur = stack[-1]
          if not cur.right and not cur.left:
            stack.pop()
            res.append(cur.val)
          if cur.right:
            stack.append(cur.right)
            cur.right = None
          if cur.left:
            stack.append(cur.left)
            cur.left = None
        return res

    def postorderTraversalRecursive(self, root):
        res = []
        self.postorderTraversalHelper(root, res)
        return res
    
    def postorderTraversalHelper(self, root, res):
        if root:
          self.postorderTraversalHelper(root.left, res)
          self.postorderTraversalHelper(root.right, res)
          res.append(root.val)

    def postorderTraversalUsingFlag(self, root):
      res = []
      stack = [(root, False)]
      while stack:
        node, visited = stack.pop()
        if node:
          if visited:
            res.append(node.val)
          else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
      return res

    def levelorderTraversal(self, root):
       return