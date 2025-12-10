from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)
from sympy import *
import sympy

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)


def doit2(ws, js):
    psyms = []

    mat = set()

    constr = []
    for i, w in enumerate(ws):
        psym = Symbol('p' + str(i), domain=S.Integers)
        psyms.append(psym)
        constr.append(psym >= 0)
        for b in w:
            mat.add((i,b))



    for j, v in enumerate(js):
        pss = []
        for i, w in enumerate(ws):
            if (i, j) in mat:
                pss.append(psyms[i])
        eq = sum(pss)
        print(j, ':', eq, '=', v)
        constr.append(Eq(eq, v))

    f = sum(psyms)

    print(constr)
    # print(f)
    r, vs = sympy.solvers.simplex.lpmin(f, constr)
    print(r, vs)
    # print()
    return r


s = 0
for l in lines:
    parts = l.split(' ')
    _, *wiring, jolt = parts
    ws = []
    for w in wiring:
        ws.append(parseints(w[1:-1], ','))
    js = parseints(jolt[1:-1], ',')
    r = doit2(ws, js)
    print(r)
    s += r

print("?")
print(s)

# 19235 no
