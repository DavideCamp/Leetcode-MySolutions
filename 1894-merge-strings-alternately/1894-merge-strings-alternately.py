class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        len_w1 = len(word1)
        len_w2 = len(word2)
        for w in range(max(len_w1, len_w2)):
            if w <= len_w1 -1:
                s = s+ word1[w]
            if w <= len_w2 -1:
                s = s+ word2[w]
        return s
            

        