class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        seen = [0]*1001
        print(seen)
        for arr in nums:
            for num in arr:
                seen[num] += 1
        res = []
        n = len(nums)
        for num, count in enumerate(seen):
            if count == n:
                res.append(num)
        return res