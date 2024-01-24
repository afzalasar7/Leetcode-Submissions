#from collection import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for i in s:
            counter[i] = counter.get(i,0) +1

        maxi_palindrome=0 
        has_single_char = False

        for value in counter.values():
            if value%2==0:
                maxi_palindrome +=value
            else:
                maxi_palindrome += value-1
                has_single_char = True
        
        if has_single_char:
            maxi_palindrome +=1

        return maxi_palindrome
