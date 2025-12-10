from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

def doit(l, machine):
    diag, ws = machine
    print(l)
    print(machine)
    mc = 99999999
    for bs in product(range(2), repeat=len(ws)):
        n = 0
        for w, b in zip(ws, bs):
            n ^= w*b
        if n == diag:
            mc = min(mc, sum(bs))
    return mc


s = 0
for l in lines:
    parts = l.split(' ')
    diag, *wiring, jolt = parts
    diag = diag[1:-1].replace('.', '0').replace('#', '1')
    diag = int(''.join(reversed(diag)), 2)
    ws = []
    for w in wiring:
        n = 0
        for b in parseints(w[1:-1], ','):
            n |= 2**b
        ws.append(n)

    machine = diag, ws
    s += doit(l, machine)

print("?")
print(s)
