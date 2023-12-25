class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_one=0
        for i in nums:
            if i == 1:
                count +=1
            else:
                count =0
            max_one = max(max_one, count)     
        return max_one        