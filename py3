class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1, w2 = sentence1.split(), sentence2.split()
        i, j, n1, n2 = 0, 0, len(w1), len(w2)
        while i < n1 and i < n2 and w1[i] == w2[i]:
            i += 1
        while j < n1 - i and j < n2 - i and w1[n1 - 1 - j] == w2[n2 - 1 - j]:
            j += 1
        return i + j == n1 or i + j == n2
