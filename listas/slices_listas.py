lista_simples_inteiro = [1, 2, 3, 8, 14, 4, 5]

print(lista_simples_inteiro[0:4])
print(lista_simples_inteiro[1:])
print(lista_simples_inteiro[:3])
nova_lista = lista_simples_inteiro[:3]
print(nova_lista)

intervalo = slice(1, 4)
print(lista_simples_inteiro[intervalo])