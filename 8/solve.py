from lib import *
import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

s = 0
boxes = set()
for l in lines:
    xyz = parseints(l, ',')
    boxes.add(tuple(xyz))
    s += 1

def dist(a, b):
    return (sum(abs(x-y)**2 for x, y in zip(a, b)))

boxes = list(boxes)
G = nx.Graph()
cs = set()
conn_dist = 0
circ = {}
cric = defaultdict(set)
nn = len(boxes)

dfa = {}
dfx = set()

for a in boxes:
    ds = []
    for b in boxes:
        if a >= b:
            continue
        d = dist(a,b)
        ds.append((d, b))
        dfx.add((d, a, b))
    ds = list(sorted(ds))
    dfa[a] = ds

dfx = list(sorted(dfx))
print("dfa ok")

for n in range(nn):
    d, a, b = dfx[n]
    print(d, a, b)
    # print
    # closest = None
    # closest_dist = 99999999
    # for d, a, b in dfx:
    #     if closest_dist > d and d > conn_dist:
    #         closest = a, b
    #         closest_dist = d

    # print(n, conn_dist, closest, closest_dist)
    # conn_dist = closest_dist
    # a, b = closest
    # c = circ.get(a) or circ.get(b) or a
    # circ[a] = c
    # circ[b] = c
    # cric[c].add(a)
    # cric[c].add(b)
    # cs.add(a)
    G.add_edge(a, b)
    # print(G.number_of_edges())

# pprint(cric)
ccs = list(nx.connected_components(G))
pprint(ccs)
# print([len(cc) for cc in reversed(sorted(nx.connected_components(G)))])
l = list(reversed(sorted([len(cr) for cr in ccs])))
a, b, c, *_ = l
print(a, b, c)
print(a * b * c)



print("?")
