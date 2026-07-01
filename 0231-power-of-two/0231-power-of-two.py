class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        elif n%2 == 1:
            return False
        else:
            for i in range(0, 32):
                if 2**i == n:
                    return True
                    break
                elif 2**i > n:
                    return False
                    break
                else:
                    pass