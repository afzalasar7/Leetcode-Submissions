class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()  # Split the sentence into words
        words.sort(key=lambda word: word[-1])  # Sort by the last character
        sorted_sentence = " ".join(word[:-1] for word in words)  # Remove digits and join
        return sorted_sentence
