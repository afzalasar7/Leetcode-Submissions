class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
        # end = len(nums)-1
        # start =0
        
        # while start <= end:
        #     mid = start +((end-start)//2)
        #     if nums[mid]< nums[mid-1] and nums[mid]<nums[mid+1]:
        #         return nums[mid]
        #     elif nums[mid] < nums[mid+1]:
        #         end = mid -1
        #     else:                
        #         start = mid+1
        nums.sort()
        return nums[0]