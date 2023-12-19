# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
        
#         nums.sort()
#         left = right = res = total = 0

#         while right < len(nums):
#             total += nums[right]

#             while nums[right] * (right - left + 1) > total + k:
#                 total -= nums[left]
#                 left += 1
            
#             res = max(res, right - left + 1)
#             right += 1
        
#         return res

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sort the array
        nums.sort()
        # Initialize the maximum frequency, window sum, and left pointer
        max_freq = 0
        window_sum = 0
        left = 0
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # Add the rightmost element to the window sum
            window_sum += nums[right]
            # While the difference between the product and the sum is greater than k
            while nums[right] * (right - left + 1) - window_sum > k:
                # Subtract the leftmost element from the window sum
                window_sum -= nums[left]
                # Move the left pointer
                left += 1
            # Update the maximum frequency with the current window size
            max_freq = max(max_freq, right - left + 1)
        # Return the maximum frequency
        return max_freq
