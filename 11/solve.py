from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

deps = {}
s = 0
for l in lines:
    d, os = l.split(': ')
    dos = []
    for o in os.split():
        dos.append(o.strip())
    d = d.strip()
    deps[d] = dos

pprint(deps)

more = [('you', [])]

while more:
    head, *more = more
    # print(head)
    (d, ps) = head

    if d == 'out':
        s += 1
        continue

    for n in deps[d]:
        more.append((n, ps+[d]))

print("?")
print(s)
