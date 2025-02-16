class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        track=0
        for ind in range(len(nums)):
            if nums[ind]!=val:
                nums[track]=nums[ind]
                track+=1
        return track

