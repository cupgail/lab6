fruits = {'Apricots': [0.9, 0, 10.5, 46],
 'Grape': [0.4, 0, 17.5, 69], 
 'Orange': [0.9, 0, 8.4, 38],
 'Ananas': [0.4, 0, 11.8, 48], 
 'Apples': [0.4, 0, 11.3, 46], 
 'Pear': [0.4, 0, 10.7, 42], 
 'Kiwi': [0.8, 0, 8.1, 47]}
nf = list(fruits.keys())
nc = list(fruits.values())

for i in range(len(nf)):
    print(i + 1, nf[i], ', '.join(str(x) for x in nc[i]))