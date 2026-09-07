class Solution(object):
    def findNthDigit(self, n):
        digits = 1
        count = 9
        start = 1
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        num = start + (n - 1) // digits
        digit = (n - 1) % digits
        return int(str(num)[digit])