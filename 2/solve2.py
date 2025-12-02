from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

def invalid(n):
    s = str(n)
    for n in range(2, len(s)+1):
        l = len(s)//n
        if s == n * s[:l]:
            return True
    return False

s = 0
for l in lines:
    ids = l.split(',')
    for rg in ids:
        print(rg)
        if not rg:
            continue
        a, b = rg.split('-')
        a, b = int(a), int(b)
        for n in range(a, b+1):
            if invalid(n):
                print(n)
                s += n

print("?")
print(s)
