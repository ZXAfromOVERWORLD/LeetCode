class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while nums:
            if len(set(nums)) == len(nums):
                return cnt
            nums = nums[3:]
            cnt += 1
        return cnt