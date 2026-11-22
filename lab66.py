n = int(input())
d = dict()
for i in range(n):
    sw = input().split()
    for k in range(len(sw)):
        d[sw[k]] = d.get(sw[k], 0) + 1

wr = max(d.values())
for w in d:
    if d[w] == wr:
        print(w)
        break