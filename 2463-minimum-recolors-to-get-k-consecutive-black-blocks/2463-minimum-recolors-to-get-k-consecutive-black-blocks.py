class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m=k
        l=0
        n=len(blocks)
        print(n)
        if n==k:
            c=blocks.count("W")
            return c
        for r in range(k,n+1):
            print(blocks[l:r])
            c=blocks[l:r].count("W")
            m=min(c,m)
            l+=1
        return m


        