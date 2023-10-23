# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         start, end = 0, len(nums)-1
#         while start<=end:
#             mid = (start + end) // 2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid] > target and nums[0]>target:
#                 start=mid+1
#             elif nums[mid] > target and nums[0]<=target:
#                 end=mid-1
#             elif nums[mid]<target:
#                 start= mid+1
#         return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                # Check if left half is sorted and if the target is in that range.
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # Right half is sorted and if the target is in that range.
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
