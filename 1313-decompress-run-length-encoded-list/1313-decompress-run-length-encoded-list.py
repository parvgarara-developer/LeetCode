class Solution(object):
    def decompressRLElist(self, nums):
        ls = []
        for num in range(0, len(nums), 2):
            ls.extend([nums[num+1]]*nums[num])
        return ls