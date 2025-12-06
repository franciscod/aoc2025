from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

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

# print(xs)
# print(ops)
# print(y)

def red(aa, op):
    if op == '+':
        f = add
    elif op == '*':
        f = mul

    r = reduce(f, aa)
    return r

for i, aa in enumerate(zip(*xs)):
    # print(aa)
    # print(ops[i])

    s += red(aa, ops[i])


print("?")
print(s)
