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
xs.add(-10000000)
ys.add(-10000000)
xs.add(10000000)
ys.add(10000000)
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
    pi = xi, yi
    psi.append(pi)
    pss.add(pi)

fpss = set()
for a, b in zip(psi, psi[1:] + psi[:2]):
    axi, ayi = a
    bxi, byi = b

    ci, di = sorted((axi, bxi))
    ei, fi = sorted((ayi, byi))

    if ei == fi:
        y = ei
        for x in range(ci, di+1):
            fpss.add((x, y))

    if ci == di:
        x = ci
        for y in range(ei, fi+1):
            fpss.add((x, y))


# empty
opss = set()
mx = len(xv)-1
my = len(yv)-1
# opss.add((0, 0))
# opss.add((0, my))
# opss.add((mx, my))
# opss.add((mx, 0))

def pmap():
    for yi, y in enumerate(yv):
        for xi, x in enumerate(xv):
            p = xi, yi
            if p in opss:
                cx = "_"
            elif p in pss:
                cx = '#'
            elif p in fpss:
                cx = 'X'
            else:
                cx = "?"

            print(end=cx)
        print()


more = [(0, 0)]
while more:
    p, *more = more

    xi, yi = p
    if not (0 <= xi <= mx):
        continue
    if not (0 <= yi <= my):
        continue

    if p in opss:
        continue

    if p in pss:
        cx = '#'
    elif p in fpss:
        cx = 'X'
    else:
        opss.add(p)

        for n in neighs(p, nd4a):
            more.append(n)

pmap()

def inside(a, b):
    axi, ayi = a
    bxi, byi = b
    ci, di = sorted((axi, bxi))
    ei, fi = sorted((ayi, byi))

    for y in range(ei, fi+1):
        for x in range(ci, di+1):
            p = x, y
            if p in opss:
                return 0

    cx, dx = xv[ci], xv[di]
    ey, fy = yv[ei], yv[fi]

    ar = (dx-cx+1)*(fy-ey+1)
    return ar

area = 0
for a in psi:
    for b in psi:
        ar = inside(a, b)
        if ar == 0:
            continue
        if area < ar:
            area = ar
            print(area)

print("?")
print(area)
# 1472215589 no, too low
# 1556350911 no, 4th guess, 5m timeout
# 1556457424 no, too high
