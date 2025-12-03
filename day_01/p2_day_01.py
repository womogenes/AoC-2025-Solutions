with open("./day_01.in") as fin:
    raw_data = fin.read().strip()
    lines = raw_data.split("\n")

count = 0
cur = 50

for line in lines:
    dir = line[0]
    amt = int(line[1:])

    for _ in range(amt):
        if dir == "L":
            cur = (cur - 1 + 100) % 100
        else:
            cur = (cur + 1) % 100

        if cur == 0:
            count += 1

print(count)
