class Solution:
    def derangeCount(self, n: int) -> int:
        # code here
        # re-occurence relation(n!=(n-1)+(n-1)!+(n-2)!)
        # 𝑛!=round(𝑛!/𝑒)
        # n!=n!.summation(-1)**k//k!
        import math
        result=0
        for k in range(n+1):
            result+=((-1)**k*math.factorial(n))//math.factorial(k)
        return result

obj=Solution()
n=int(input())
print(obj.derangeCount(n))
