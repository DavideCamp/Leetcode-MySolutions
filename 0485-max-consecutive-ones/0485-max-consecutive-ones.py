class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        res = []
        for i in nums:
            if i == 1:
                n = n + 1 
            else:
                res.append(n)
                n = 0
        res.append(n)
        return max(res)
        