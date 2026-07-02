import numpy as np
class Solution(object):
    def shiftGrid(self, grid, k):
        grid1 = np.array(grid)
        flat = grid1.flatten()
        sh = np.roll(flat, shift=k)
        res = sh.reshape(grid1.shape)
        return res.tolist()