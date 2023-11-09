class Solution(object):
    def isAnagram(self, s, t):
        sort_s = sorted(s)
        sort_t = sorted(t)
        return sort_s == sort_t
