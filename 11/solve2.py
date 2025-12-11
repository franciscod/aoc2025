from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

deps = {}
s = 0
# print("digraph {")
for l in lines:
    d, os = l.split(': ')
    d = d.strip()
    dos = []
    for o in os.split():
        no = o.strip()
        dos.append(no)
        # print(f"{d} -> {no}")
    deps[d] = dos

# print("}")
# pprint(deps)

more = [{'svr':(False, False, 1)}]

count = 0
while more:
    head, *more = more
    ks = head

    nks = {}
    for k, v in ks.items():
        pd, pf, n = v
        pd = pd or k == 'dac'
        pf = pf or k == 'fft'
        if k == 'out':
            if pd and pf:
                s += n
            continue

        for j in deps[k]:
            v = nks.get(j, (pd, pf, 0))
            npd, npf, nn = v
            nks[j] = (npd, npf, nn + n)

    if nks:
        more.append(nks)
        count += 1
        # pprint(nks)

print("?")
print(s)
