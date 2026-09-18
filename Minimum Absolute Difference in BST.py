'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        ret=float('inf')
        prv=-float('inf')
        def dfs(cur=root):
            nonlocal ret,prv
            if not cur:
                return
            dfs(cur.left)
            ret=min(ret,cur.data-prv)
            prv=cur.data
            dfs(cur.right)
        dfs()
        return ret
        
