class Solution(object):
    def guessNumber(self, n):
        i = 1
        while i <= n:
            mid = (i + n) // 2
            res = guess(mid)
            if res == 0:
                return mid   
            elif res == 1:
                i = mid + 1
            elif res == -1:
                n = mid - 1