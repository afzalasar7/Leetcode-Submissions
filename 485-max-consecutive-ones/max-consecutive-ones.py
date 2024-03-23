class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        ans = 0
        for i in nums:
            if i == 0:
                ans=max(ans, curr)
                curr=0
            else:
                curr+=1
        ans=max(ans, curr)

        return ans