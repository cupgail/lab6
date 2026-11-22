n = int(input())
dc = dict()
for i in range(n):
    cc = input().split()
    country = cc[0]
    cities = cc[1:len(cc)]
    dc[country] = cities    

ld = list()
m = int(input())
for k in range(m):
    ld.append(input().strip())

for cities in ld:
    for country in dc:
        if cities in dc[country]:
            print(country)