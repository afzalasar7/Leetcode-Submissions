class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = max(max(left) if left else 0,n-min(right) if right else 0)
        return ans
        