class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        iDepth = 0
        core = ""
        maxlencore = 0     
        for i in range(1, len(s) - 1):
            if s[i] == s[i - 1]:
                iDepth = iDepth + 1
            if s[i] == s[i + 1]:
                if i < len(s) - 2:
                    continue
                else:
                    i = i + 1
                    iDepth = iDepth + 1      
            if iDepth > 0:
                core = s[i] * (iDepth + 1)
            else:
                core = s[i]         
            depth = len(s) - i - 1 if len(s) - i - 1 < i - iDepth else i - iDepth
            k = 1
            for j in range(i - iDepth - 1, i - iDepth - depth - 1, -1):
                if s[j] != s[i + k]:
                    break
                else:
                    core = s[j] + core + s[j]
                k = k + 1
            if len(core) > maxlencore:
                res = core
                maxlencore = len(core)
            iDepth = 0
        return res