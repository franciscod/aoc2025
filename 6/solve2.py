from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)
import operator

lines = inputlines(nostrip=True)
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

s = 0
xs = []
y = None
ops = []
op = False

for l in lines:
    try:
        i = parseints(l)
        if not op:
            xs.append(i)
        else:
            y = i
    except:
        ops = l.split()
        op = True

ns = []
for l in lines:
    ns.append(l)

def red(aa, op):
    if op == '+':
        r = 0
        f = operator.add
    elif op == '*':
        r = 1
        f = operator.mul

    for a in aa:
        r = f(r, a)
    return r

su = 0
op = None
args = []
for col in zip(*ns):
    skip = False
    if col[0] == '\n':
        skip = True
    if not skip:
        mop = col[4]
        if mop != ' ':
            op = mop

        s = ''.join(col[:4]).strip()
    if (not skip) and (tuple(col) != (' ', ' ', ' ', ' ', ' ')):
        n = int(s)
        args.append(n)
    else:
        print(args, op)
        r = red(args, op)
        su += r
        args = []

print("?")
print(su)
