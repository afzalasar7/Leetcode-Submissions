class Solution:
    def minPairSum(self, nums):
        result = 0
        nums.sort()
        while nums:
            max_num = nums.pop(-1)
            min_num = nums.pop(0)
            result = max(result, max_num + min_num)
        return result
        
        