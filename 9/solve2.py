from lib import *

lines = inputlines()

ps = []
for l in lines:
    x, y = parseints(l, ',')
    ps.append((x, y))

xs = set()
ys = set()
for x, y in ps:
    xs.add(x)
    ys.add(y)

xv = list(sorted(xs))
yv = list(sorted(ys))

psi = []
for x, y in ps:
    xi = xv.index(x)
    yi = yv.index(y)
    pi = xi, yi
    psi.append(pi)

fpss = set()
for a, b in zip(psi, psi[1:] + psi[:2]):
    axi, ayi = a
    bxi, byi = b

    ci, di = sorted((axi, bxi))
    ei, fi = sorted((ayi, byi))

    for y in range(ei, fi+1):
        for x in range(ci, di+1):
            fpss.add((x, y))


def inside(a, b):
    axi, ayi = a
    bxi, byi = b
    ci, di = sorted((axi, bxi))
    ei, fi = sorted((ayi, byi))
    for p in fpss:
        pxi, pyi = p
        if ci < pxi < di and ei < pyi < fi:
            return 0

    cx, dx = xv[ci], xv[di]
    ey, fy = yv[ei], yv[fi]

    ar = (dx-cx+1)*(fy-ey+1)
    return ar

area = 0
for a in psi:
    for b in psi:
        ar = inside(a, b)
        if area < ar:
            area = ar

print("?")
print(area)
