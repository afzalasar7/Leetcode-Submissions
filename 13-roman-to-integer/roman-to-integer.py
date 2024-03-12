class Solution:
    def romanToInt(self, s: str) -> int:
        value={"I":1,"V":5,"X":10,"L":50,"C":100, "D":500,"M":1000}
        l = len(s)-1
        
        sum = 0
        for i in range(l):
            if value[s[i]] < value[s[i+1]]:
                sum-=value[s[i]]
            else:
                sum+= value[s[i]]
        sum+=value[s[-1]]

        return sum
        