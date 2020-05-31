class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        def helper(root):
            if not root:
                return
            out.append(root.val)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)

        helper(root)
        return out

    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        stack = [root]
        if not root:
            return out
        while stack:
            element = stack.pop()
            out.append(element.val)
            if element.right:
                stack.append(element.right)
            if element.left:
                stack.append(element.left)
        return out

