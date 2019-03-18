'''
Funções

Permite a reutilização do código, através de blocos específicos
'''

from a021_aula08_funcoes_criadas import *

# Se quiser utilizar alias
# import a021_aula08_funcoes_criadas as funcs

# Definição da função
def saudacao():
    print('Hello World!')

# Chamada da função
saudacao()

print('\n')

soma(1, 5)

print('\n')

sub(1, 5)
sub(b=1, a=5) # Especifica a ordem

print('\n')

calc(3, 5, 'soma')
calc(5, 3, 'sub')
calc(3, 6)

print('\n')

resultado = calc_soma(1, 2)

print(resultado)

print('\n')

pessoa = cria_pessoa('Devair', 'Computação')
print(pessoa)

print('\n')

nomes = ['Lea', 'Eddie']
exibe_usuarios(nomes)

print('\n')

notas = [5, 5, 6, 7, 2]
print(notas)

altera_notas(notas)
print(notas)

# Para que seja passada uma cópia, não alterando o próprio
# objeto, basta chamar dessa maneira altera_notas(notas[:])

print('\n')

imprime_notas('Eddie', 5)
imprime_notas('Lea', 5, 5, 7, 9)