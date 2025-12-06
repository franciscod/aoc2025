from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)
import operator

lines = inputlines()
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

print(xs)
print(ops)
print(y)

for i, aa in enumerate(zip(*xs)):
    # print(aa)
    # print(ops[i])

    r = 0
    if ops[i] == '+':
        r = 0
        f = operator.add
    elif ops[i] == '*':
        r = 1
        f = operator.mul

    for a in aa:
        r = f(r, a)
    s += r


print("?")
print(s)
