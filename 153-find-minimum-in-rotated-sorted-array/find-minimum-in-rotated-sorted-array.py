class Solution:
    def findMin(self, nums: List[int]) -> int:
        res =nums[0]
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] >= nums[0]:
                start = mid+1
            elif nums[mid] < nums[0]:
                res = nums[mid]
                end = mid-1
        return res