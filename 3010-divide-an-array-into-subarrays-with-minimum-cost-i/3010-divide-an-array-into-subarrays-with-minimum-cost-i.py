class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        mini = nums[0]
        nums.pop(0)
        min1 = min(nums)
        nums.remove(min1)
        min2 = min(nums)
       
        return mini + min1 + min2