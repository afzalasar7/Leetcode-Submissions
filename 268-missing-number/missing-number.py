class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expect = (n * (n + 1)) // 2 
        return expect - sum(nums)