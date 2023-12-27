class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        from collections import Counter
        hash = {}

        for i in nums:
            hash[i] = hash.get(i, 0) +1


        
            
        major = len(nums)//2
        for i, v in hash.items():
            if v>major:
                return i
        