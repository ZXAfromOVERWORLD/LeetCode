class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        j=len(nums)-1
        i=0
        while (i<=j):
            if nums[i]!=val:
                i+=1
                continue
            nums[i]=nums[j]
            j-=1


        return i
            
        
        