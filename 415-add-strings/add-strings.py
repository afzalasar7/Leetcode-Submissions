class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1

        # Iterate until either string is exhausted or there's no carry
        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            sum_of_digits = digit1 + digit2 + carry

            carry = sum_of_digits // 10
            result = chr(sum_of_digits % 10 + ord('0')) + result  # Prepend digit

            i -= 1
            j -= 1

        return result
