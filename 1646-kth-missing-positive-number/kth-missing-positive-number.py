class Solution:
    # O(log(n)) time | O(1) space
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)
        while left < right:
            middle = (left + right) // 2
            if arr[middle] - middle - 1 < k:
                left = middle + 1
            else:
                right = middle
        return left + k