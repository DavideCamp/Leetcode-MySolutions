class Solution(object):
    def twoSum(self, nums, target):
        diz = {}
        for i, num in enumerate(nums):
            if target - num in diz:
                return [diz[target-num] , i]
            else:
                diz[num] = i
