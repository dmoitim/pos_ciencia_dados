def soma(a, b): # Recebe dois argumentos
    print(str(a + b))

def sub(a, b): # Recebe dois argumentos
    print(str(a - b))

def calc(a, b, op='soma'): # Esppecifica valor padrão
    if op == 'soma':
        soma(a, b)
    elif op == 'sub':
        sub(a, b)

def calc_soma(a, b):
    resultado = a + b
    return resultado

# Função retornando dicionário
def cria_pessoa(nome, curso):
    pessoa = {'nome': nome, 'curso': curso}
    return pessoa

# Função utilizando lista
def exibe_usuarios(nomes):
    for nome in nomes:
        print(nome)

# Função alterando a própria lista do programa (de fora)
def altera_notas(notas):
    for i in range(0, len(notas)):
        notas[i] += 10

def imprime_notas(nome, *notas): # Não sei quantas notas eu terei
    print('Aluno(a) ' + nome)
    for nota in notas:
        print(nota)
    print('')