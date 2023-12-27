class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffmap  = {}

        for i, v in enumerate(nums):
            if target-v in diffmap:
                return [i, diffmap[target-v]]
            diffmap[v] = i


           


            







    