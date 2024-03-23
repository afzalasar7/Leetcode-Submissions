# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # l=0
#         # for i in range(len(nums)):
#         #     if nums[i]:
#         #         nums[l], nums[i] = nums[i], nums[l]
#         #         l+=1
#         nums.sort(key=lambda x: x == 0)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  # Pointer for non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]  # Swap non-zero element with element at j
                j += 1  # Increment j to point to the next position for non-zero element
