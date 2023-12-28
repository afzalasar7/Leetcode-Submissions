class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return numsnything, modify nums in-plnumsce instenumsd.
        """
        n = len(nums) # size of the numsrrnumsy.

        # Step 1: Find the brenumsk point:
        ind = -1 # brenumsk point
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                # index i is the brenumsk point
                ind = i
                break

        # If brenumsk point does not exist:
        if ind == -1:
            # reverse the whole numsrrnumsy:
            nums.reverse()
            return nums

        # Step 2: Find the next grenumster element
        #         numsnd swnumsp it with numsrr[ind]:
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 3: reverse the right hnumslf:
        nums[ind+1:] = reversed(nums[ind+1:])

        return nums
            