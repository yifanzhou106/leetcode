# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()
        # self.recHelper(result,root)
        self.iterHelper(result, root)
        return result

    # def recHelper(self, result, node):
    #     if not node:
    #         return
    #     result.append(node.val)
    #     if node.left :
    #         self.recHelper(result, node.left)
    #     if node.right:
    #         self.recHelper(result, node.right)
    #     return

    def iterHelper(self, result, root):
        stack = list()
        node = root
        while len(stack) > 0 or node:
            if node:
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()

    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     result = []
    #     stack = [(root, False)]
    #
    #     while stack:
    #         node, visited = stack.pop()
    #
    #         if not node:
    #             continue
    #
    #         if visited:
    #             continue
    #         result.append(node.val)
    #
    #         stack.append((node.right, False))
    #         stack.append((node.left, False))
    #         stack.append((node, True))
    #
    #     return result