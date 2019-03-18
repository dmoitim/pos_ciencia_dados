'''
    Calcula a popularidade de linguagens de programação em uma
    escola de informática.
    Crie um dicionário e armazene a entrada do nome da pessoa e
    a linguagem que ela programa (1) C++ - (2) Java - (3) Python
    e ao final imprima quantos votos cada linguagem obteve
'''

linguagens = {}

qtd_alunos = int(input('Informe a quantidade de alunos da escola: '))

for i in range(0, qtd_alunos):
    nome = input('Digite seu nome: ')
    linguagem = int(input('Digite a linguagem (1) C++ - (2) Java - (3) Python: '))

    if linguagem == 1:
        linguagens[nome] = 'C++'
    elif linguagem == 2:
        linguagens[nome] = 'Java'
    else:
        linguagens[nome] = 'Python'

# print(linguagens)

c = 0
java = 0
python = 0

for valor in linguagens.values():
    if valor == 'C++':
        c += 1
    elif valor == 'Java':
        java += 1
    else:
        python += 1

print('\nResultado')
print('C++: ' + str(c))
print('Java: ' + str(java))
print('Python: ' + str(python))