class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr+=1
            else:
                curr=0
            ans=max(ans, curr)
        return ans