class Solution:
    def isPalindrome(self, x: int) -> bool:
        #number = str(x)
        # length = len(number)
        # for i in range(len(number)//2):
        #     if number[i] != number[length -1-i]:
        #         return False
        # return True
        # if len(number) %2==0:
        #     return True if number[:len(number)//2] == number[(len(number)//2):len(number)] else False
        # else:
        #     return True if number[:len(number)//2] == number[(len(number)//2)+1:len(number)] else False
        # return True if number[:len(number)//2] == number[len(number)-1:(len(number)//2)+1:-1] else False

        rev = 0
        y = x
        while y>0:
            rev = rev*10 + y%10
            y = y// 10

        return True if x == rev else False