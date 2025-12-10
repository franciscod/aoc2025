from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)


# from pulp import *
def doit2_pulp(ws, js):
    prob = LpProblem("myProblem", LpMinimize)
    psyms = []

    mat = set()
    constr = []
    for i, w in enumerate(ws):
        psym = LpVariable('p' + str(i), 0, 1000, LpInteger)
        psyms.append(psym)
        constr.append(psym >= 0)
        for b in w:
            mat.add((i,b))
    f = sum(psyms)
    prob += f


    for j, v in enumerate(js):
        pss = []
        for i, w in enumerate(ws):
            if (i, j) in mat:
                pss.append(psyms[i])
        eq = sum(pss)
        prob += eq == v


    # print(constr)
    # print(f)
    prob.solve(PULP_CBC_CMD(msg=0))
    r = 0
    for v in prob.variables():
        r += v.varValue
    # print()
    return int(r)

def doit2(ws, js):
    buttons = len(ws)
    counters = len(js)

    A = np.zeros((buttons, counters))
    for i, wr in enumerate(ws):
        for b in wr:
            A[i, b] = 1
    b = np.array(js)
    c = np.ones(buttons)

    # minimize c @ x
    # such that
    #   A_ub @ x <= b_ub
    #   A_eq @ x == b_eq
    #   lb <= x <= ub
    res = scipy.optimize.linprog(c, A_eq=A.T, b_eq=b, integrality=1)
    assert res.status == 0
    x = res.x
    return sum(round(n) for n in x)

s = 0
for l in lines:
    parts = l.split(' ')
    _, *wiring, jolt = parts
    ws = []
    for w in wiring:
        ws.append(parseints(w[1:-1], ','))
    js = parseints(jolt[1:-1], ',')
    r = doit2(ws, js)
    # print(r)
    s += r

print("?")
print(s)
