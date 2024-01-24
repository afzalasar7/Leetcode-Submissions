#from collection import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for i in s:
            counter[i] = counter.get(i,0) +1
        maxi_palindrome=0

        for key, value in counter.items():
            if value%2==0:
                maxi_palindrome += value
                counter[key] = 0

            else:
                if value>2:
                    maxi_palindrome += value-1
                    counter[key] = 1


        for value in counter.values():
            if value == 1:
                maxi_palindrome +=1
                break
        return maxi_palindrome


        