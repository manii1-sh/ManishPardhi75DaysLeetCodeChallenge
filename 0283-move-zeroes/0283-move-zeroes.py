class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  # pointer for placing non-zero elements
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1