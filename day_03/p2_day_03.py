from functools import lru_cache

with open("./day_03.in") as fin:
    lines = fin.read().strip().split("\n")

ans = 0

@lru_cache(None)
def get_max_jolt(line, pick):
    if pick == 0:
        return ""
    
    if len(line) == 0:
        return ""

    n = len(line)
    if n == pick:
        return line
    
    c1 = line[0] + get_max_jolt(line[1:], pick - 1)
    c2 = get_max_jolt(line[1:], pick)

    return max(c1, c2)

# print(get_max_jolt("54321", 2))
# exit()

for line in lines:
    # print(line)
    max_jolt = get_max_jolt(line, 12)
    ans += int(max_jolt)

print(ans)
