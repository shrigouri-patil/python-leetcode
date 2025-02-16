class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for ind in range(0,len(nums)):
            if nums[ind]==nums[-1]:
                return len(nums)
            elif nums[ind]==nums[ind+1]:
                nums.remove(nums[ind])
        

