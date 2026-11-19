class Solution:
    def sortIt(self, arr):
        arr.sort(key=lambda x:-x if x%2==1 else x)
