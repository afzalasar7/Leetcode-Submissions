class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        last =-1
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = start +((end-start)//2)
            if target == nums[mid]:
                first =mid
                end=mid-1
            elif nums[mid]> target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1

        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = start +((end-start)//2)
            if target == nums[mid]:
                last =mid
                start=mid+1
            elif nums[mid]> target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
        return [first,last]
        
        