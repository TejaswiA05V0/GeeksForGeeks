class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        sm=0
        for i in range(1,n):
            sm+=i
            if i>=2 and (n-sm)%i==0:
                return True
            if n<=sm:
                return False

