minha_tupla = (1, 2, 3, "Olá, Mundo", 1.5)
minha_tupla2 = 1, 2, 3, "Olá, Mundo", 1.5, True

print(type(minha_tupla))
print(type(minha_tupla2))

# count()
print(minha_tupla.count(1))

# index()
print(minha_tupla.index(3))

# verificar a existencia de um elemento na tupla
print(22 in minha_tupla)

print(minha_tupla.__add__(minha_tupla2))