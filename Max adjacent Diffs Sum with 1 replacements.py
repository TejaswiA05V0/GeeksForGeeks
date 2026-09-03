class Solution:
    def maxDiffSum(self, arr):
        # code here
        stay, change = 0, 0
        for i in range(1, len(arr)):
            stay_e = arr[i]
            change_e = 1
            nstay = max(abs(stay_e - 1)+change, abs(stay_e - arr[i-1]) +stay)
            nchange = max(abs(change_e - 1)+change, abs(change_e - arr[i-1])+stay)
            stay, change = nstay, nchange
        return max(stay, change)
