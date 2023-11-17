class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        lst = []
        nums.sort()

        ptr1 = 0
        ptr2 = len(nums) - 1
        while ptr1 < ptr2:
            lst.append(nums[ptr1]+nums[ptr2])
            ptr1 += 1
            ptr2 -= 1
        
        return max(lst)

