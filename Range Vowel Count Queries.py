class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        pfs=[0]
        for c in s:
            pfs.append(pfs[-1]+int(c in 'aeiou'))
        return [pfs[r+1]-pfs[l] for l,r in queries]
