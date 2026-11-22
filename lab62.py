e2g = {'stork': 'storch', 'hawk': 'falke', 
       'woodpecker': 'specht', 
       'owl': 'eule'} #Can use any other words
a = list(e2g.items())

for i in range(len(a)):
    b = list(a[i])
    print(f'{b[0]}:', b[1])