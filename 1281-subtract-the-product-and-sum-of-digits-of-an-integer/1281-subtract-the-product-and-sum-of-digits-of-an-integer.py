class Solution(object):
    def subtractProductAndSum(self, n):
        n1 = list(map(int, str(n)))
        total_sum = sum(int(i) for i in n1)
        total_product = 1
        for digit in n1:
            total_product *= int(digit)
        res = total_product - total_sum
        return res