class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        newIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[newIndex] = nums[i]
                newIndex += 1

        for i in range(newIndex, len(nums)):
            nums[i] = 0
        return nums
        