'''
Laços while

Se repete até que uma condição é atingida, ou seja, não sabemos
quantas vezes a ação será executada
'''

contador = 1
while contador <= 5: # Executa até que o contador seja igual a 6
    print(contador)
    contador += 1

print('\n')

mensagem = ''
while mensagem != 'sair':
    mensagem = input("Escreva 'sair' para terminar: ")
    if mensagem != 'sair':
        print(mensagem)

print('\n')

flag = True
while flag:
    mensagem = input("Escreva 'sair' para terminar: ")
    if mensagem == 'sair':
        flag = False
    else:
        print(mensagem)

print('\n')

while True:
    mensagem = input("Escreva 'sair' para terminar: ")
    if mensagem == 'sair':
        break
    else:
        print(mensagem)

print('\n')

print('Imprime os números ímpares:')
contador = 0
while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue # Pula para a próxima execução do laço

    print(contador)

print('\n')

# While em listas e dicionários
materiais = ['caneta', 'caderno', 'livro', 'lápis']
objetos = []

while materiais:
    objeto = materiais.pop() # Remove o último elemento da lista
    objetos.append(objeto)

for objeto in objetos:
    print(objeto.title())

# Preenchendo um dicionário
linguagens = {}

flag = True
while flag:
    nome = input('Informe seu nome: ')
    linguagem = input('Informe a linguagem de programação: ')

    # Armazena a resposta no dicionário
    linguagens[nome] = linguagem

    resposta = input('Há mais alguém para responder? (s/n): ')
    if resposta == 'n':
        flag = False

for nome, linguagem in linguagens.items():
    print(nome.title() + ' tem preferência pela linguagem ' + linguagem + '.')