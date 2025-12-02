with open("./day_02.in") as fin:
    ranges = fin.read().split(",")

def invalid(x):
    s = str(x)
    if len(s) % 2 == 1:
        return False
    
    n = len(s)
    return s[:n//2] == s[n//2:]

ans = 0
for r in ranges:
    a, b = list(map(int, r.split("-")))

    for x in range(a, b + 1):
        if invalid(x):
            ans += x

print(ans)
