class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        mp = {}
        ans = [-1, -1, -1, -1]

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                s = arr[i] + arr[j]

                if s in mp:
                    p = mp[s]

                    if (p[0] != i and p[0] != j and
                        p[1] != i and p[1] != j):

                        if (ans[0] == -1 or
                            p[0] < ans[0] or
                            (p[0] == ans[0] and p[1] < ans[1]) or
                            (p[0] == ans[0] and p[1] == ans[1] and i < ans[2]) or
                            (p[0] == ans[0] and p[1] == ans[1] and
                             i == ans[2] and j < ans[3])):

                            ans = [p[0], p[1], i, j]

                if s not in mp:
                    mp[s] = [i, j]

        return ans
