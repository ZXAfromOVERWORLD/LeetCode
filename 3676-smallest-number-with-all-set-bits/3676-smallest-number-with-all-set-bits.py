class Solution:
    def smallestNumber(self, n: int) -> int:
        s=bin(n)
        n="1"*(len(s)-2)
        return (int(n,2))
        
        
            
        