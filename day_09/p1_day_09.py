with open("./day_09.in") as fin:
    lines = fin.read().strip().split("\n")

coords = [list(map(int, line.split(","))) for line in lines]

n = len(lines)

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = coords[i]
        x2, y2 = coords[j]

        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        ans = max(ans, area)

print(ans)
