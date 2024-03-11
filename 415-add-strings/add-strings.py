class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        i = len(num1)-1
        j = len(num2) -1
        while i >=0 or j >=0 or carry:
            digit1 = ord(num1[i]) - ord("0") if i >= 0 else 0
            digit2 = ord(num2[j]) - ord("0") if j >= 0 else 0
            sumOfDigit = digit1 + digit2 + carry
            carry = sumOfDigit // 10
            # result = chr(sumOfDigit % 10 + ord("0")) + result
            result = f"{sumOfDigit%10}{result}" 
            i -=1
            j -=1
        return result