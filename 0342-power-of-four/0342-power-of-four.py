class Solution(object):
    def isPowerOfFour(self, n):
        if n==1:
            return True
        elif n%2 == 0:
            i = 1
            for i in range(31):
                if n < 4**i:
                    return False
                elif n == 4**i:
                    return True
        else:
            return False