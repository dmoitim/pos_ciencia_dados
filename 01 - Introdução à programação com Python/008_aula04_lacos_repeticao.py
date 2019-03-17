'''
Laços de repetição

Iteração para realizar um mesmo conjunto de instruções
'''

materiais = ['caneta', 'caderno', 'livro', 'e-book']

# Imprime a lista inteira
print(materiais)

# Loop para iteração nos elementos da lista
for material in materiais:
    print(material)
    print(material.title())

print('\n')

# Realiza loop de 1 até 4 - 1 (inclusive) e 5 (menos 1)
for valor in range(1, 5):
    print(valor)

print('\n')

# Realiza loop de 1 até 4 - criando a lista com o comando range
numeros = list(range(1, 5))
for valor in numeros:
    print(valor)

print('\n')

# Realiza loop para exibir o quadrado dos números de 1 a 10
quadrados = []
for valor in range(1, 11):
    quadrado = valor ** 2
    quadrados.append(quadrado)

print(quadrados)

# Imprime o menor valor da lista
print(min(quadrados))

# Imprime o maior valor da lista
print(max(quadrados))

# Imprime a soma do valor de todos os elementos da lista
print(sum(quadrados))

print('\n')

# Manipulando parte da lista

# Imprime os elementos de índices 0, 1 e 2
print(materiais[0:3])

# Imprime os elementos de índices 1, 2 e 3
print(materiais[1:4])

# Imprime os elementos de índices 2 até o último
print(materiais[2:])

# Imprime os elementos de índices 0 até 2
print(materiais[:3])

print('\n')

# Realiza cópia da lista inteira
objetos = materiais[:]

# Se fizéssemos como a linha abaixo, elas estariam referenciando
# o mesmo local na memória, logo ambas listas seriam modificadas
# objetos = materiais

print(materiais)
print(objetos)

objetos.append('cola')

print(materiais)
print(objetos)

print('\n')

# Repetições aninhadas

# Tabuada do 2 e do 3
for i in range(2, 4):
    print('Tabuada do ' + str(i))
    for j in range(1, 11):
        print(str(i) + ' x ' + str(j) + ' = ' + str(i * j))
    print('\n')

