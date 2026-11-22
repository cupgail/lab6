stud = {'S 001': ['Math', 'Computer Science'],
        'S 002': ['Math', 'English'],
        'S 003': ['Philosophy', 'English', 'Physical training']}

a = list(stud.keys())
b = list()
print(stud)

for i in range(len(a)):
    c = a[i].replace(' ', '')
    b.append(c)

for n in range(len(a)):
    stud[b[n]] = stud[a[n]]
    del stud[a[n]]

print(stud)