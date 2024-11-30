class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        s.add(0)
        for i in range(0,100+len(nums)):
            if i not in s:
                return i
            
        