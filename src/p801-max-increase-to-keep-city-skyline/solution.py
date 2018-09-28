class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """Compute how much we can increase the heights of a grid of buildings
        without altering its skyline when viewed from any side.
        :type grid: List[List[int]]
        :rtype: int
        """
        transpose = lambda a: [[a[c][r] for c in range(len(a))] for r in range(len(a))]
        length = width = len(grid)
        row_maxs = [max(row) for row in grid]
        col_maxs = [max(col) for col in transpose(grid)]
        increase = 0
        for i in range(length):
            for j in range(width):
                new_height = min(row_maxs[i], col_maxs[j])
                curr_height = grid[i][j]
                increase += (new_height - curr_height)
        return increase
