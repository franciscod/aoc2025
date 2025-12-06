from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)
import operator

lines = inputlines(nostrip=True)
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

s = 0

def red(aa, op):
    if op == '+':
        f = add
    elif op == '*':
        f = mul

    r = reduce(f, aa)
    return r

op = None
args = []
for col in zip(*lines):
    if col[0] == '\n':
        s += red(args, op)
        break

    mop = col[4]
    if mop != ' ':
        op = mop

    l = ''.join(col[:4]).strip()
    if tuple(col) != (' ', ' ', ' ', ' ', ' '):
        n = int(l)
        args.append(n)
    else:
        # print(args, op)
        s += red(args, op)
        args = []

print("?")
print(s)
