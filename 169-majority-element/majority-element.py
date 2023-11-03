class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        from collections import Counter
        hash = Counter(nums)
        major = len(nums)//2
        for i, v in hash.items():
            if v>major:
                return i