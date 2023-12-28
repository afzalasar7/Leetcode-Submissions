class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # sort the array
        nums.sort()
        lastSmaller = float('-inf')
        cnt = 0
        longest = 1

        # find longest sequence
        for i in range(n):
            if nums[i] - 1 == lastSmaller:
                # a[i] is the next element of the
                # current sequence
                cnt += 1
                lastSmaller = nums[i]
            elif nums[i] != lastSmaller:
                cnt = 1
                lastSmaller = nums[i]
            longest = max(longest, cnt)
        return longest