meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}
meu_dicionario_2 = {'nome': 'João', 'sobrenome': 'Silva', 'idade': 50}

#get()
print(meu_dicionario[2])
print(meu_dicionario.get(2))

print(meu_dicionario_2.get('sobrenome'))

#len()
print(len(meu_dicionario))

#pop()
meu_dicionario.pop(2)
print(meu_dicionario)

#clear()
#meu_dicionario.clear()
print(meu_dicionario)

#keys()
print(meu_dicionario.keys())
print(meu_dicionario_2.keys())

#Adicionando elementos
meu_dicionario[5] = 'Joaquina'
print(meu_dicionario)
meu_dicionario_2.update({'profissao': 'Programador'})
print(meu_dicionario_2)