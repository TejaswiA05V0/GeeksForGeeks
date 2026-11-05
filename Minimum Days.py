class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        st=set()
        lth=len(s)
        for ix in range(1,lth):
            if s[ix-1]==s[ix]:
                st.add(ix-1)
        if not st:
            return 0
        for ix,ve in enumerate(p):
            st.discard(ve)
            st.discard(ve-1)
            if not st:
                return ix+1
        return -1
