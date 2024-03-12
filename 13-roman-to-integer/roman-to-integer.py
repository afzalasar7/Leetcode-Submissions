class Solution:
    def romanToInt(self, s: str) -> int:
        value={"I":1,
        "V" : 5,
        "X":10,
        "L":50,
        "C" :100,
        "D":500,
        "M":1000,
        "IV":4,
        "IX":9,
        "XL":40,
        "XC":90,
        "CD":400,
        "CM":900
        }

        doubleChar = ["IV",
        "IX",
        "XL",
        "XC",
        "CD",
        "CM"]
        sum = 0
        # for item in doubleChar:
        #     if item in s:
        #         sum+=value[item]
        #         s = s.replace(item, "")
        # for char in s:
        #     sum+= value[char]
        i=0
        l= len(s)-1
        while i < l:
            if value[s[i]] < value[s[i+1]]:
                sum-=value[s[i]]
            else:
                sum+= value[s[i]]
            i+=1
        sum+=value[s[-1]]

        return sum
        