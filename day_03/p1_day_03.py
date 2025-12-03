with open("./day_03.in") as fin:
    lines = fin.read().split("\n")

ans = 0

for line in lines:
    max_jolt = 0
    n = len(line)
    for i in range(n):
        for j in range(i + 1, n):
            jolt = int(line[i] + line[j])
            max_jolt = max(max_jolt, jolt)

    ans += max_jolt

print(ans)
