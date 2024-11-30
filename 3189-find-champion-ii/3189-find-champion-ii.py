class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        s=set()
        l=set([i for i in range(n)])
        if edges==[] and n==1:
            return 0
        for i in edges:
            s.add(i[1])
        print(l)
        print(s)
        s=l.difference(s)
        print(s)
        if len(s)!=1:
            return -1
        return list(s)[0]
            


        