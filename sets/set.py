# Declaração de um set
meu_set = {1, 2, 3, 4, 1}
print(type(meu_set))

meu_set_2 = set([1, 2, 8, 9, 10])
print(type(meu_set_2))

# add()
meu_set.add(2)
print(meu_set)

# update()
meu_set.update([3, 4, 5, 6])
print(meu_set)

# discard()
meu_set.discard(2)
print(meu_set)

# União
print(meu_set | meu_set_2)
print(meu_set.union(meu_set_2))

# Interseção
print(meu_set & meu_set_2)
print(meu_set.intersection(meu_set_2))

# Diferença
print(meu_set - meu_set_2)
print(meu_set_2.difference(meu_set))

# Diferença Simétrica
print(meu_set ^ meu_set_2)
print(meu_set.symmetric_difference(meu_set_2))
