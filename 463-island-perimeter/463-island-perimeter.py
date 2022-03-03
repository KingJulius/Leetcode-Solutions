class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visitSet = set()
        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visitSet:
                return 0
            visitSet.add((i,j))
            perim = dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1) + dfs(i-1, j)
            return perim
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    return dfs(i, j)
        
        return 0
