class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        has_odd_char = False
        ans = 0
        for i in s:
            counter[i] = counter.get(i, 0) +1

        for v in counter.values():
            if v % 2 == 0:
                ans += v
            else:
                ans += v-1
                has_odd_char = True
        return ans+1 if has_odd_char else ans


