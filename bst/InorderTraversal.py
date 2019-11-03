# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [(root, False)]
        result = []
        while len(stack) > 0:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                result.append(node.val)
                continue
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))

        return result

