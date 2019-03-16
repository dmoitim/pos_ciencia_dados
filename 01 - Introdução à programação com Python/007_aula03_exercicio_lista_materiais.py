'''
    Lista de materiais:
'''

materiais = ['caneta', 'caderno', 'livro', 'lápis']

# Imprimir a lista na tela:
print(materiais)

# Adicione um novo material
materiais.append('borracha')

# Imprima a posição em que o novo material foi adicionado
materiais[-1]

# Ordene a lista de forma ascendente e a imprima novamente
materiais.sort()
print(materiais)

# Mostre o tamanho da lista
print(str(len(materiais)))

# Remova um dos elementos e imprima a lista novamente
materiais.remove('caderno')
print(materiais)