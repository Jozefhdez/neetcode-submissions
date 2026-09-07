class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        stack = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    grid[i][j] = "0"
                    stack.append((i, j))

                    while stack:
                        curr_i, curr_j = stack.pop()
                        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            newi, newj = curr_i + di, curr_j + dj
                            if n > newi >= 0 and m > newj >= 0 and grid[newi][newj] == "1":
                                grid[newi][newj] = "0"
                                stack.append((newi, newj))

        return ans