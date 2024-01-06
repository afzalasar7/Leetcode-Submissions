class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 1 , len(nums)-2
        if nums[-2] != nums[-1]:
            return nums[-1]
        if nums[1] != nums[0]:
            return nums[0]
        while l<=r:
            mid = (l+r) // 2
            if nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            if (mid%2 ==1 and nums[mid-1] == nums[mid]) or (mid%2 ==0 and nums[mid+1] == nums[mid]):
                l=mid+1
            else:
                r =mid-1
        return -1