string = input()
counter = {letter: string.count(letter) for letter in string}
for i in range(len(counter.keys())):
    klst = list(counter.keys())
    print(klst[i], counter[klst[i]])