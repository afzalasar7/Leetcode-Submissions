class Solution:
    def recursive_bin_search(self, arr, target, high, low):
        if high<low:
            return -1
        mid = (high + low) //2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            self.recursive_bin_search(arr, target, mid-1, low)
        else:
            self.recursive_bin_search(arr, target, high, mid+1)

    def search(self, nums: List[int], target: int) -> int:
        start , end = 0, len(nums)-1
        while start<=end:
            mid = (start + end) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid -1
            elif nums[mid] < target:
                
                start= mid+1
        return -1
        #return (self.recursive_bin_search(nums, target, len(nums)-1, 0))
        