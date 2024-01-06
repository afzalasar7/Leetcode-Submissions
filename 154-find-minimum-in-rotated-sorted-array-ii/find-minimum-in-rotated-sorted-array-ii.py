class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:  # Continue until start and end meet
            mid = start + (end - start) // 2

            if nums[mid] > nums[end]:  # Left side is unrotated
                start = mid + 1
            elif nums[mid] < nums[end]:  # Right side is unrotated
                end = mid
            else:  # Handle duplicates by moving both pointers inwards
                end -= 1

        return nums[start]