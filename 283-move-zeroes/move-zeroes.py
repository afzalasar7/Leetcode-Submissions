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
        index = 0

        # Place non-zero elements at the start of the list
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1

        # Fill the remaining positions with zeroes
        while index < len(nums):
            nums[index] = 0
            index += 1