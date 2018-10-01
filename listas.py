lista_simples_inteiro = [1, 2, 3, 8, 14, 4, 5]
listas_simples_string = ["Olá", "Mundo"]
lista_simples_mesclada = [1, 2, 3, "Olá, mundo", True, 1.5]
nested_list = [[1, 2, True], ["Olá", "mundo"]]

print(lista_simples_inteiro)
print(nested_list)

# Len()
print(len(lista_simples_mesclada))
print(len(nested_list))

# Append()
lista_simples_inteiro.append(6)
print(lista_simples_inteiro)

# Insert()
#lista_simples_inteiro.insert(2, "Olá")
#print(lista_simples_inteiro)

# Remove()
lista_simples_inteiro.remove(1)
print(lista_simples_inteiro)

# Index()
index = lista_simples_inteiro.index(3)
print(index)

# Count()
count = lista_simples_inteiro.count(3)
print(count)

# Sort()
lista_string = ["A", "B", "C"]
lista_string.sort(reverse=True)
print(lista_string)