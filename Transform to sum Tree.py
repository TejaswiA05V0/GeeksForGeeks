''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        # code here
        def convert(node):
            if node is None:
                return 0
            left_sum = convert(node.left)
            right_sum = convert(node.right)
            old_val = node.data
            node.data = left_sum + right_sum
            return node.data + old_val
        convert(root)
