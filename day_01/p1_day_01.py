with open("./day_01.in") as fin:
    raw_data = fin.read().strip()
    lines = raw_data.split("\n")

count = 0
cur = 50
for line in lines:
    dir = line[0]
    amt = int(line[1:])
    print(dir, amt)

    if dir == "L":
        cur = (cur - amt + 100) % 100
    else:
        cur = (cur + amt) % 100

    print(cur)
    if cur == 0:
        count += 1

print(count)
