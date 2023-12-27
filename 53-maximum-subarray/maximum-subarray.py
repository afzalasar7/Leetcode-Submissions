class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum =nums[0]
        currSum = 0
        for i in nums:
            if currSum<0:
                currSum =0
            currSum+=i
            maxSum = max (currSum, maxSum)
        return maxSum


       