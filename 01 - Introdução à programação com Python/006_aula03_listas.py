'''
Listas

Forma simples de interligar elementos de um conjunto.
Estrutura que possui as operações de inserção, exclusão e localização de elementos
'''

materiais = ['caneta', 'caderno', 'livro', 'lápis']

# Imprime a lista inteira
print(materiais)

# Imprime o primeiro elemento da lista
print("Primeiro elemento da lista: " + materiais[0])

# Imprime o último elemento da lista
print("Último elemento da lista: " + materiais[-1])

# Alterando o valor de um elemento
materiais[2] = 'ebook'

# Imprime a lista inteira
print(materiais)

# Incluindo um elemento no final da lista
materiais.append('cola')

# Incluindo um elemento em uma posição específica da lista
materiais.insert(0, 'tesoura')

# Imprime a lista inteira
print(materiais)

# Removendo elemento específico da lista
del materiais[0]

# Removendo o último elemento da lista
elemento_removido = materiais.pop()

# Removendo elemento específico da lista
elemento_removido_pop = materiais.pop(2)

# Removendo elemento específico da lista
materiais.remove('caderno')

# Imprime a lista inteira
print(materiais)

# Imprime elemento removido da lista
print("Elemento removido da lista: " + elemento_removido)

# Imprime elemento removido da lista (pop)
print("Elemento removido da lista (pop): " + elemento_removido_pop)

# Ordenação da lista
sobremesas = ['sorvete', 'bolo', 'pudim', 'brigadeiro', 'sonho']
print(sobremesas)

sobremesas.reverse() # Inverte a lista
print(sobremesas)

sobremesas.sort() # Ascendente
print(sobremesas)

sobremesas.sort(reverse=True) # Descendente
print(sobremesas)

# Tamanho da lista
print("A lista possui " + str(len(sobremesas)) + " elementos")