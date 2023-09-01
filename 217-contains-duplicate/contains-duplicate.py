class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j =0
        for i in range(len(nums)-1):
            j = i+1
            if nums[i] == nums[j]:
                return True
        return False

