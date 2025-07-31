class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        lenght = len(nums)
        if lenght == 1:
            return nums
        for i in range(lenght - 1):
            if i == 0:
                res.append(nums[i])
            res.append(res[i] + nums[i+1])
        return res
        