def eleva_dois(max = 0):
    n = 0
    while n <= max:
        yield 2 ** n
        n += 1

for i in eleva_dois(5):
    print(i)