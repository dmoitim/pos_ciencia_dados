'''
Dicionários

Permite definir elementos com chave / valor
'''

# Define o dicionário
pessoa = {
    'nome': 'Lea',
    'idade': 21
}

# Imprime as propriedades do dicionário, através da chave
print(pessoa['nome'])
print(pessoa['idade'])

# Adicionando nova chave / valor
pessoa['curso'] = 'Computação'

# Alterando um valor
pessoa['idade'] = 19

# Imprime dicionário
print(pessoa)

# Removendo chave
del pessoa['curso']

# Imprime dicionário
print(pessoa)

# Cria um dicionário vazio
pessoa2 = {}

# Adicionando nova chave / valor
pessoa2['curso'] = 'Moda'

# Imprime dicionário
print(pessoa2)

print('\n')

linguagens = {
    'lea': 'python',
    'sara': 'c',
    'eddie': 'java',
    'phil': 'python'
}

print('A linguagem usada poe Lea é: ' + linguagens['lea'].title())

print('\n')

# Loop no dicionário, retornando chave e valor
for chave, valor in pessoa.items():
    print('Chave: ' + str(chave))
    print('Valor: ' + str(valor))

print('\n')

# Loop no dicionário, retornando somente as chaves
for chave in sorted(pessoa.keys()): # sorted, ordena as chaves
    print('Chave: ' + str(chave))

print('\n')

# Loop no dicionário, retornando somente as chaves
for valor in pessoa.values():
    print('Valor: ' + str(valor))

print('\n')

# Aninhamento de dicionários
pessoa01 = {'nome': 'Lea', 'idade': 25}
pessoa02 = {'nome': 'Eddie', 'idade': 21}
pessoa03 = {'nome': 'Phil', 'idade': 23}

pessoas = [pessoa01, pessoa02, pessoa03]

for pessoa in pessoas:
    print(pessoa)

print('\n')

# Criando listas dentro de um dicionário
pessoa001 = {
    'nome': 'Lea',
    'curso': 'Computação',
    'linguagens': ['python', 'c', 'java']
}

print(pessoa001)

print('\n')

for linguagem in pessoa001['linguagens']:
    print(linguagem.title())

print('\n')

# Criando um dicionário em um dicionário
pessoas_dic = {
    'leasilva': {
        'nome': 'Lea',
        'sobrenome': 'Silva',
        'curso': 'Computação'
    },
    'eddiesilva': {
        'nome': 'Eddie',
        'sobrenome': 'Silva',
        'curso': 'Computação'
    }
}

for username, userinfo in pessoas_dic.items():
    print('Usuários: ' + username)
    for chave, valor in userinfo.items():
        print(chave + ': ' + valor)
    print()