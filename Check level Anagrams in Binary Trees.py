"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""


class Solution:

    def areAnagrams(self, root1, root2):
        """ code here """

        q1, q2 = [root1], [root2]

        v1, v2 = [], []
        while q1 and q2:
            for _ in range(len(q1)):
                node = q1.pop(0)
                v1.append(node.data)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            for _ in range(len(q2)):
                node = q2.pop(0)
                v2.append(node.data)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            if sorted(v1) != sorted(v2):
                return False
        if not q1 and not q2:
            return True
        return False
