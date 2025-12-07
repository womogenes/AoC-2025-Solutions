from collections import defaultdict

with open("./day_07.in") as fin:
    lines = fin.read().strip().split("\n")

start_col = lines[0].index("S")
beam_cols =  defaultdict(int)
beam_cols[start_col] = 1

n, m = len(lines), len(lines[0])

timelines = 0

for row in range(1, n):
    new_cols = defaultdict(int)
    splitter_cols = [i for i in range(m) if lines[row][i] == "^"]

    for bc, count in beam_cols.items():
        hit = False
        for sc in splitter_cols:
            if bc == sc:
                timelines += count
                new_cols[sc - 1] += count
                new_cols[sc + 1] += count
                hit = True
                break

        if not hit:
            new_cols[bc] += count

    beam_cols = new_cols

print(sum(beam_cols.values()))
