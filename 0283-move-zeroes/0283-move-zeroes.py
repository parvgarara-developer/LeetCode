class Solution:
    def moveZeroes(self, nums):
        non_zero = [x for x in nums if x]
        nums[:] = non_zero + [0] * (len(nums) - len(non_zero))