'''
    Soma 1 números inteiros fornecido pelo teclado:
'''

lista = 0

for num in range(1, 11):
    lista += int(input('Digite o ' + str(num) + 'º um número: '))

print('A soma de todos os números é ' + str(lista))