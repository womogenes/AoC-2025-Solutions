with open("./day_07.in") as fin:
    lines = fin.read().strip().split("\n")

start_col = lines[0].index("S")
beam_cols = [start_col]

n, m = len(lines), len(lines[0])

splits = 0

for row in range(1, n):
    new_cols = set()
    splitter_cols = [i for i in range(m) if lines[row][i] == "^"]

    for bc in beam_cols:
        hit = False
        for sc in splitter_cols:
            if bc == sc:
                new_cols.add(sc - 1)
                new_cols.add(sc + 1)
                hit = True
                splits += 1
                break

        if not hit:
            new_cols.add(bc)

    beam_cols = list(new_cols)

print(splits)
