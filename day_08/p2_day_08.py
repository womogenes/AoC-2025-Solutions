from collections import defaultdict

with open("./day_08.in") as fin:
    lines = fin.read().strip().split("\n")

points = [tuple(map(int, line.split(","))) for line in lines]

n = len(points)

def dist_sq(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))

# dists = [[0] * n for _ in range(n)]
dists = {}
for i in range(n):
    for j in range(i + 1, n):
        dists[(i, j)] = dist_sq(points[i], points[j])

dists_arr = sorted(dists.items(), key=lambda pair: pair[1])

adj = defaultdict(list)

# Union-find
par = {i: i for i in range(n)}
size = {i: 1 for i in range(n)}

def get_par(i):
    global par
    if par[i] == i:
        return i
    return get_par(par[i])

TOP = 10 if n < 25 else 1000
for edge, _ in dists_arr:
    i, j = edge
    pi, pj = get_par(i), get_par(j)
    
    if pi == pj:
        continue

    par[pi] = pj
    size[pj] += size[pi]

    if size[pj] == n:
        xi = points[i][0]
        xj = points[j][0]
        print(xi * xj)

        break
