class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size = min(len(word1), len(word2))
        merged=""
        for i in range(size):
            merged+= word1[i]
            merged+= word2[i]

        if len(word1) >len(word2):
            merged+= word1[len(word2):]
        else:
            merged+= word2[len(word1):]
        return merged
        