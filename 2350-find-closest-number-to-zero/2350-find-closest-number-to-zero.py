class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closed_to_0 = sorted(nums)[0]
        for n in sorted(nums):
            if n == 0:
                return n
            if n > closed_to_0 and n < 0:
                closed_to_0 = n
            if n < closed_to_0 and n > 0:
                closed_to_0 = n
            if n > 0 and closed_to_0 < 0:
                pos_n = closed_to_0 * -1 
                closed_to_0 = n if n <= pos_n else closed_to_0
        return closed_to_0

        