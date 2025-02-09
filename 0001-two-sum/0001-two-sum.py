class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind1 in range(0,len(nums)-1):
            for ind2 in range(ind1+1,len(nums)):
                if nums[ind1]+nums[ind2]==target: 
                    return [ind1,ind2]

