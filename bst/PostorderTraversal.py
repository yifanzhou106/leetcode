# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if not node:
                continue

            if visited:
                result.append(node.val)
                continue

            stack.append((node.left, False))
            stack.append((node.right, False))
            stack.append((node, True))

        result.reverse()
        return result
