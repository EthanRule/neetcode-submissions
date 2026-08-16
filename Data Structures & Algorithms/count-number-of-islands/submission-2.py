class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate over the grid, when we encounter land, run 2d dynamic
        # progamming alg to set all land to 0 until no land is left, then 
        # increment islands count. Skip over 2's in the future.

        # 2D island scan alg
        def dfs(grid, i, j):
            # 2, 0, and bounds base case
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == '2' or grid[i][j] == '0':
                return
            grid[i][j] = '2'

            # NORTH
            dfs(grid, i - 1, j)
            # EAST
            dfs(grid, i, j + 1)
            # SOUTH
            dfs(grid, i + 1, j)
            # WEST
            dfs(grid, i, j - 1)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    islands += 1
        return islands

        