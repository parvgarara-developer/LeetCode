class Solution(object):
    def hasAlternatingBits(self, n):
        b = str(bin(n)[2:])
        if '11' in b:
            return False
        elif '00' in b:
            return False
        else:
            return True