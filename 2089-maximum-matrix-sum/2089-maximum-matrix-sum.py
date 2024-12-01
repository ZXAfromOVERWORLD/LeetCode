@cache
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        l=[]
        count=0
        flag=0
        zero=0
        s=0
        for i in matrix:
            l.extend(i)
        l.sort()
        for i in l:
            if i<0:
                count+=1
        if 0 in l:
            for i in l:
                s+=abs(i)
        elif count%2==0:
            for i in l:
                s+=abs(i)
        else:
            for i in range(len(l)):
                l[i]=abs(l[i])
            l.sort()
            l[0]*=-1
            s=sum(l)
        return s

        