from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

ps = []
s = 0
for l in lines:
    x, y = parseints(l, ',')
    # print(x, y)
    s += 1
    ps.append((x, y))

mps = {}
area = 0

xs = set()
ys = set()
xs.add(-9999999)
ys.add(-9999999)
xs.add(9999999)
ys.add(9999999)
for x, y in ps:
    xs.add(x)
    ys.add(y)

xv = list(sorted(xs))
yv = list(sorted(ys))

psi = []
pss = set()
for x, y in ps:
    xi = xv.index(x)
    yi = yv.index(y)
    psi.append((xi, yi))
    pss.add((xi, yi))

def kof(a, b):
    if a < b:
        return '<'
    if a == b:
        return '='
    if a > b:
        return '>'

fill = {}
fpss = set()
for z, a, b in zip(psi[-1:] + psi[:-1], psi, psi[1:] + psi[:2]):
    zxi, zyi = z
    axi, ayi = a
    bxi, byi = b

    zx, zy = xv[zxi], yv[zyi]
    ax, ay = xv[axi], yv[ayi]
    bx, by = xv[bxi], yv[byi]

    # kind = ''.join( [
    #             '',
    #             kof(zx, ax),
    #             kof(zy, ay),
    #             ' ',
    #             kof(ax, bx),
    #             kof(ay, by),
    #             ])

    # print(zx, zy)
    # print(ax, ay)
    # print(bx, by)
    # # print(kind)
    # ks = kind.split(' ')

    # name = {
    #         '=>': "up",
    #         '<=': "right",
    #         '=<': "down",
    #         '>=': "left",
    #     }

    # kname = name[ks[0]], "then", name[ks[1]]

    # fa = "?"
    # if kind == "=> <=":
    #     # up then right
    #     fa = "++"
    # elif kind == "<= =<":
    #     # right then down
    #     fa = "-+"
    #     pass
    # elif kind == "=< >=":
    #     # down then left
    #     fa = "--"
    #     pass
    # elif kind == ">= =>":
    #     # left then up
    #     fa = "+-"
    #     pass
    # elif kind == "=> >=":
    #     # up then left
    #     fa = "-+"
    #     pass
    # elif kind == "<= =>":
    #     # right then up
    #     fa = "--"
    #     pass
    # elif kind == ">= =<":
    #     # left then down
    #     fa = "++"
    #     pass
    # elif kind == "=< <=":
    #     # down then right
    #     fa = "+-"
    #     pass
    # else:
    #     raise ValueError

    # ox = 0
    # oy = 0
    # if fa[0] == '-': ox = -0.5
    # if fa[0] == '+': ox =  0.5
    # if fa[1] == '-': oy = -0.5
    # if fa[1] == '+': oy =  0.5

    # fill[axi+ox, ayi+oy] = "X"


    # print(a, kind, kname, fa)

    ci, di = sorted((axi, bxi))
    ei, fi = sorted((ayi, byi))

    for y in range(ei, fi+1):
        for x in range(ci, di+1):
            fpss.add((x, y))

opss = set()
mx = len(xv)-1
my = len(yv)-1
opss.add((0, 0))
opss.add((0, my))
opss.add((mx, my))
opss.add((mx, 0))

for yi, y in enumerate(yv):
    for xi, x in enumerate(xv):
        p = xi, yi
        if (xi, yi) in pss:
            cx = '#'
        elif (xi, yi) in fpss:
            cx = 'O'
        elif (xi, yi) in opss:
            cx = ' '
        else:
            for n in neighs(p, nd4a):
                if n in opss:
                    opss.add(p)
for yi, y in reversed(list(enumerate(yv))):
    for xi, x in reversed(list(enumerate(xv))):
        p = xi, yi
        if (xi, yi) in pss:
            cx = '#'
        elif (xi, yi) in fpss:
            cx = 'O'
        elif (xi, yi) in opss:
            cx = ' '
        else:
            for n in neighs(p, nd4a):
                if n in opss:
                    opss.add(p)

for yi, y in enumerate(yv):
    for xi, x in enumerate(xv):
        p = xi, yi
        if p in opss:
            cx = "_"
        else:
            cx = "X"

        # if (xi, yi) in pss:
        #     cx = '#'
        # elif (xi, yi) in fpss:
        #     cx = 'O'
        # elif (xi, yi) in opss:
        #     cx = '.'
        # else:
        #     cx = '='
        print(end=cx)
    print()

def inside(a, b):
    axi, ayi = a
    bxi, byi = b
    ci, di = sorted((axi, bxi))
    ei, fi = sorted((ayi, byi))

    for y in range(ei, fi+1):
        for x in range(ci, di+1):
            p = x, y
            if p in opss:
                return False

    return True

print(len(xv))
print(len(yv))
area = 0
ma, mb = 0, 0
for a in psi:
    for b in psi:

        if not inside(a, b):
            continue

        axi, ayi = a
        bxi, byi = b

        ax, ay = xv[axi], yv[ayi]
        bx, by = xv[bxi], yv[byi]

        ar = (abs(bx-ax)+1)*(abs(by-ay)+1)

        if area < ar:
            area = ar
            ma = a
            mb = b
            #print(area, a, b)

axi, ayi = ma
bxi, byi = mb
ci, di = sorted((axi, bxi))
ei, fi = sorted((ayi, byi))

for yi, y in enumerate(yv):
    for xi, x in enumerate(xv):
        p = xi, yi

        if (ci <= xi <= di) and (ei <= yi <= fi):
            cx = "O"
        else:
            if p in opss:
                cx = " "
            elif p in pss:
                cx = "#"
            else:
                cx = "."

        print(end=cx)
    print()

print("?")
print(area)
# 1472215589 no, too low
# 1556457424 no, too high
