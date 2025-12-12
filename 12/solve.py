from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = iter(inputlines())
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

shapes = []
s = 0
for l in lines:
    n, *_ = parseints(l+"0", ':')
    m = []
    m.append(next(lines))
    m.append(next(lines))
    m.append(next(lines))
    rows, cols, mp, rmp = readmp(m)
    shapes.append(mp)
    next(lines)
    if n == 5:
        break

for l in lines:
    w, h, *counts = parse("{:d}x{:d}: {:d} {:d} {:d} {:d} {:d} {:d}", l)

    lens = [len(m) for m in shapes]
    a = w*h

    t = 0
    for c, l in zip(counts, lens):
        t += c*l

    if t*1.2 > a:
        print("discard")
        continue
    print(f"{t=} {a=}")



    print(counts)
    s += 1


print("?")
print(s)
