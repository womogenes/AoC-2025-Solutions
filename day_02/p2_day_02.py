with open("./day_02.in") as fin:
    ranges = fin.read().split(",")

def get_divisors(n):
    for m in range(1, n):
        if n % m == 0:
            yield m

def invalid(x):
    s = str(x)
    
    n = len(s)
    for m in get_divisors(n):
        if s == s[:m] * (n // m):
            return True

    return False

ans = 0
for r in ranges:
    a, b = list(map(int, r.split("-")))
    print(len(str(b)), b < 1e10)

    for x in range(a, b + 1):
        if invalid(x):
            ans += x

print(ans)
