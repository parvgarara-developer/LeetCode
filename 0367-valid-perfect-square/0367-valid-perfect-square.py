class Solution(object):
    def isPerfectSquare(self, num):
        if sqrt(num)-int(sqrt(num)) != 0:
            return False
        else:
            return True