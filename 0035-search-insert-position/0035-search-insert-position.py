class Solution(object):
    def searchInsert(self, nums, target):
        l = nums
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                l.append(target)
                l.sort()
                return l.index(target)

