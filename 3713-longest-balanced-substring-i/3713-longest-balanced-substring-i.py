class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        length = len(s)
        if length == 1: return 1
        for i in range(length):
            sub = {s[i]:1}
            for j in range(i + 1, length):
                sub[s[j]] = sub[s[j]] + 1 if s[j] in sub else 1
                if res < len(sub) * sub[s[j]] and len(set(sub.values())) <= 1:
                    res = len(sub) * sub[s[j]]
        return res


      


        