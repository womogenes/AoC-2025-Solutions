with open("./day_05.in") as fin:
    ranges, ids = fin.read().strip().split("\n\n")

ranges = [tuple(map(int, line.split("-"))) for line in ranges.split("\n")]
ids = list(map(int, ids.split("\n")))

print(ranges, ids)

ans = 0
fresh = set()

for i in ids:
    for a, b in ranges:
        # if i in range(a, b + 1):
        if a <= i <= b:
            fresh.add(i)

ans = len(fresh)
print(ans)
