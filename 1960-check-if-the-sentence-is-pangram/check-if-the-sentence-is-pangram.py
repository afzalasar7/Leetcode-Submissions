class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #return True if len(set(sentence)) >=26 else False
        ans = [0]*26
        a = ord("a")
        for i in sentence:
            ans[ord(i)-a] += 1

        for i in ans:
            if i<1:
                return False
        return True
