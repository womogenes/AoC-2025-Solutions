from functools import lru_cache

with open("./day_09.in") as fin:
    lines = fin.read().strip().split("\n")

coords = [list(map(int, line.split(",")))[::-1] for line in lines]
n = len(lines)

x = [c[0] for c in coords]
y = [c[1] for c in coords]

min_x, max_x = min(x), max(x)
min_y, max_y = min(y), max(y)

print(max_x - min_x, max_y - min_y)

edges = []
for i in range(n):
    p1 = coords[i]
    p2 = coords[(i + 1) % n]
    edges.append((p1, p2))

@lru_cache(None)
def in_poly(row, col):
    parity = 0

    for p1, p2 in edges:
        # print(p1, p2)

        # Does it cross this edge?
        if p1[0] == p2[0]:
            # Horizontal edge
            y = p1[0]
            x1, x2 = min(p1[1], p2[1]), max(p1[1], p2[1])

            if row < y:
                continue
            
            elif row == y:
                if x1 <= col <= x2:
                    # On the line
                    return True
                
            else:
                assert row > y
                # print("crossed horizontal edge")
                
                if x1 <= col < x2:
                    parity += 1

        else:
            # Different column?
            if p1[1] != col:
                continue

            # Vertical edge
            y1, y2 = min(p1[0], p2[0]), max(p1[0], p2[0])

            if row > y2:
                continue

            elif row < y1:
                continue
                
            else:
                return True

    return parity % 2


# for i in range(16):
#     for j in range(16):
#         if in_poly(i, j):
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

def is_valid_rect(p1, p2):
    x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
    y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])

    for x in range(x1, x2):
        if not in_poly(x, y1) or not in_poly(x, y2):
            return False
    
    for y in range(y1, y2):
        if not in_poly(x1, y) or not in_poly(x2, y):
            return False
            
    return True

ans = 0

from tqdm import tqdm

for i in tqdm(range(n)):
    for j in tqdm(range(i + 1, n)):
        if not is_valid_rect(coords[i], coords[j]):
            continue

        x1, y1 = coords[i]
        x2, y2 = coords[j]

        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        ans = max(ans, area)

print(ans)
