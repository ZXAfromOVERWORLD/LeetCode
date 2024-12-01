class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s=set(arr)
        if arr.count(0)==1:
            s.remove(0)
        for i in arr:
            if 2*i in s:
                return True
        return False
        