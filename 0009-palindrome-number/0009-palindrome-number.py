class Solution(object):
    def isPalindrome(self, x):
        strx = str(x)
        return strx == strx[::-1]