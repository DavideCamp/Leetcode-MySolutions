class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        diz = {}
        
        for i, num in enumerate(numbers):
            if target - num in diz:
                return [diz[target-num] , i+1]
            else:
                diz[num] = i +1