class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        d = Counter(nums)
        total =0
        for k,value in d.items():
            if value==1:
                total+= k

        return total