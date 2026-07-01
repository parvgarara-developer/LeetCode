class Solution(object):
    def plusOne(self, digits):
        num = int("".join(map(str, digits)))
        arr = [int(digit) for digit in str(num+1)]
        return arr