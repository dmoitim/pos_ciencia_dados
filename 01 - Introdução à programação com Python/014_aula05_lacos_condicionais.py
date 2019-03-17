'''
Laços de condição

Permite o programa decidir o caminho a ser seguido

Operadores relacionais

>   maior
>=  maior ou igual
<   menor
<=  menor ou igual
==  igual
!=  diferente

Operadores lógicos
AND e
OR  ou
'''

carros = ['audi', 'bmw', 'subaru', 'toyota']

# Loop
for carro in carros:
    #Teste condicional
    if carro == 'bmw': # Se verdadeiro
        print(carro.upper())
    else: # Senão
        print(carro.title())

# Exemplo com operador AND
idade = int(input('Digite sua idade: '))
if idade >= 18 and idade <= 69:
    print('Seu voto é obrigatório!')
else:
    print('Seu voto NÃO é obrigatório!')

# Exemplo com operador OR
nota = int(input('Digite sua nota: '))
frequencia = int(input('Digite sua frequência: '))
if nota < 60 or frequencia < 25:
    print('Reprovado(a)!')
else:
    print('Aprovado(a)!')

# Verificando valores em listas
materiais = ['caneta', 'caderno', 'livro', 'e-book']
condicao = 'caneta' in materiais
print('caneta existe em materiais: ' + str(condicao))
condicao = 'agenda' in materiais
print('agenda existe em materiais: ' + str(condicao))

# Exemplo com elif
idade = int(input('Digite sua idade: '))

if idade < 4: # Se
    print('Sua entrada custa R$ 0,00')
elif idade < 18: # Senão, se
    print('Sua entrada custa R$ 5,00')
elif idade < 65: # Senão, se
    print('Sua entrada custa R$ 10,00')
else: # Senão
    print('Sua entrada custa R$ 8,00')

