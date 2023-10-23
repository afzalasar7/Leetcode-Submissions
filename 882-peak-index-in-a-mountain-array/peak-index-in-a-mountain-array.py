class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        end = len(arr)-1
        start =0
        while start <= end:
            mid = start +((end-start)//2)
            if arr[mid]> arr[mid-1] and arr[mid]> arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                start = mid+1
            else:
                end = mid -1
            