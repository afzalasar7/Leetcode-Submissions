class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major = len(nums)/3
        major_elements =[]
        for num in set(nums):
            if nums.count(num) > major:
                major_elements.append(num)
        return major_elements