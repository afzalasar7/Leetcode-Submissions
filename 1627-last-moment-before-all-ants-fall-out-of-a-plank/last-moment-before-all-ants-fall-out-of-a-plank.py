class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # Find the farthest position among ants moving to the left.
        maxLeft = max(left, default=0)

        # Find the nearest position among ants moving to the right.
        minRight = n - min(right, default=n)

        # Calculate the time when the last ant(s) fall.
        return max(maxLeft, minRight)