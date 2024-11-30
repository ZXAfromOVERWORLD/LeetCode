class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s=set(nums)
        if len(nums)==0:
            return 0
        elif target in s:
            return(nums.index(target))
        else:
            s.add(target)
            l=sorted(s)
            print(l)
            return(l.index(target))
        