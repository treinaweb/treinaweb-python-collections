meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}
print(type(meu_dicionario))
meu_dicionario_2 = dict({1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'})
print(type(meu_dicionario_2))

print(meu_dicionario[4])

for chave, valor in meu_dicionario.items():
    print(f" A chave é {chave} e o valor {valor}")