class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        def square(n):
            return (n * n)
        for i in nums:
            array.append(square(i))

        array = sorted(array, key=float)
        return array

