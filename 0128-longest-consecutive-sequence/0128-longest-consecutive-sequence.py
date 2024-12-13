class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        print(nums)
        l=0
        r=1
        k=1
        m=1
        while (r<=len(nums)-1):
            if nums[l]+k==nums[r]:
                r+=1
                k+=1
                continue
            else:
                m=max(k,m)
                k=1
                l=r
                r+=1
        m=max(k,m)
        return m


        