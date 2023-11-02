class Solution:
    def bitwiseComplement(self, n: int) -> int:
        #generate a new number
        if n == 0:
            return 1
        m = n
        mask = 0
        while (m!=0):
            #generate a mask
            mask = (mask << 1) | 1
            m = m >> 1
        answer = (~n) & mask
        
        return answer
        
        

        
        