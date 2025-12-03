from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

# greedy, by santy
def maxbank(bank, k, s=0):
    r = ""
    da = len(bank) - k
    for d in bank:
        while r and da and r[-1] < d:
            r = r[:-1]
            da -= 1
        r += d
    return int(r[:k])


# dp, slow
@cache
def maxbank_dp(bank, k, s=0):
    n = 0
    if k == 0:
        return 0
    for i0, v0 in enumerate(bank):
        if i0 < s:
            continue
        # print(i0, v0)
        rv = maxbank(bank, k-1, i0+1)
        if rv == 0:
            rv = ""
        v = int(v0 + str(rv))
        n = max(n, v)

    # print(n)
    return n



s = 0
for r in range(rows):
    # print(r, "...")
    bank = ""
    for c in range(cols):
        bank += mp[r,c]
    b = maxbank(bank,12)
    s += b

print("?")
print(s)
