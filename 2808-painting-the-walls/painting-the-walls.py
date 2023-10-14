class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        nwalls = len(cost)
        dp = [sum(cost) for _ in range(nwalls + 1)]
        dp[0] = 0
        for i, c in enumerate(cost):
            for t in range(nwalls, 0, -1):
                if dp[max(t-time[i]-1, 0)] + c < dp[t]:
                    dp[t] = dp[max(t-time[i]-1, 0)] + c
        return dp[-1]