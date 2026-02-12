class Solution:
 
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = {}
        lista = list(s)
        if len(s) < 2 :
           return len(s)
        for i, l in enumerate(lista):
            res = [l]
            for j  in range(i + 1, len(s)):
                if lista[j] in res:
                    substrings[len(res)] = ''.join(res)
                    break
                if lista[j] not in res:
                    res.append(lista[j])
            substrings[len(res)] = ''.join(res)
        return max(substrings.keys())
                    