class Solution:
    def sortVowels(self, s: str) -> str:
        ans = []
        vowel_temp=[]
        for char in s:
            if char in "aeiouAEIOU":
                vowel_temp.append(char)
                ans.append("#")
            else:
                ans.append(char)
        vowel_temp.sort()
        ptr=0
        for i in range(len(ans)):
            if ans[i] == "#":
                ans[i] = vowel_temp[ptr]
                ptr+=1
        return "".join(ans)