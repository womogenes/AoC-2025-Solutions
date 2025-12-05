with open("./day_04.in") as fin:
    grid = fin.read().strip().split("\n")

n, m = len(grid), len(grid[0])


dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def can_get(i, j):
    count = 0

    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == dj == 0:
                continue
            ii, jj = i + di, j + dj
            if not (0 <= ii < n and 0 <= jj < m):
                continue

            count += grid[ii][jj] == "@"

    return count < 4


ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "@" and can_get(i, j):
            ans += 1

print(ans)
