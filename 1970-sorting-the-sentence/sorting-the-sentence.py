class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")  # Split the sentence into words
        ans = [0] * len(words)
        for word in words:
            index = int(word[-1]) - 1  # Adjust for 0-based indexing
            ans[index] = word[:-1]  # Assign the word without the digit
        return " ".join(ans)  # Join the sorted words into a sentence
