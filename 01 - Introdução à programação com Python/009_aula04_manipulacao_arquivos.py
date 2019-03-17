'''
Leitura e gravação de arquivos
'''

# Leitura de arquivo
arquivo = open('010_aula04_arquivo_pessoas.txt', 'r')

for linha in arquivo:
    lista = linha.split() # Split pelo espaço criando lista
    print(lista)

arquivo.close()

# Gravação de arquivo
materiais = ['caneta', 'caderno', 'livro', 'e-book']
arquivo = open('011_aula04_arquivo_escrito.txt', 'w')

for material in materiais:
    arquivo.write('Material: ' + material + '\n')

arquivo.close()