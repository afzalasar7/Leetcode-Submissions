# class Solution:
#     def longestPalindrome(self, s: str) -> int:
        # counter = {}
        # has_odd_char = False
        # ans = 0
        # for i in s:
        #     counter[i] = counter.get(i, 0) +1

        # for v in counter.values():
        #     if v % 2 == 0:
        #         ans += v
        #     else:
        #         ans += v-1
        #         has_odd_char = True
        # return ans+1 if has_odd_char else ans
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        pairs=0
        extra=0
        
        for count in counts.values():
            pairs += count // 2
            extra += count % 2
            
        return 2 * pairs + (1 if extra else 0)

