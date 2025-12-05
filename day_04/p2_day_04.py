with open("./day_04.in") as fin:
    grid = [list(line) for line in fin.read().strip().split("\n")]

n, m = len(grid), len(grid[0])

def can_get(i, j):
    global grid

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

while True:
    more = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "@" and can_get(i, j):
                grid[i][j] = "."
                more += 1
    
    if more == 0:
        break

    ans += more

print(ans)
