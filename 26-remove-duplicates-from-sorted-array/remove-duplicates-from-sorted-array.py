class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n =len(nums)
        point= 1
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[point] = nums[i]
                point+=1
            
        return point