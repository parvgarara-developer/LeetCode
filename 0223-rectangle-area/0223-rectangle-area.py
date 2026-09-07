class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        ax3 = ax2 - ax1
        ay3 = ((ay2 - ay1))
        by3 = ((by2 - by1))
        bx3 = ((bx2 - bx1))
        a1 = ax3 * ay3
        b1 = bx3 * by3
        cx = max(0, min(ax2, bx2) - max(ax1, bx1))
        cy = max(0, min(ay2, by2) - max(ay1, by1))
        c1 = cx * cy
        return (a1 + b1 - c1)