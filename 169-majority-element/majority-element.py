class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # from collections import Counter
        # hashMap = Counter(nums)
        # for i in hashMap:
        #     if hashMap[i] > len(nums)//2:
        #         return i

        res,count = 0,0
        for i in nums:
            if count == 0:
                res = i
            count+= 1 if i == res else -1
        return res