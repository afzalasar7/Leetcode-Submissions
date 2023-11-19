class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        curr = nums[0]
        add = 0
        for num in nums:
            if num != curr:
                add+=1
                curr= num
            res+=add
        
        return res
        