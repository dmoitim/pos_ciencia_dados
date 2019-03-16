'''
    Caculadora:
    Recebe dois números (inteiros ou decimais) digitados pelo usuário
    e realiza a soma, subtração, multiplicação e divisão de ambos, ou
    a raiz quadrada do primeiro número
    e exibe o resultado na tela
'''

import math

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
raiz = math.sqrt(num1)

print("Soma: " + str(soma))
print("Subtração: " + str(subtracao))
print("Multiplicação: " + str(multiplicacao))
print("Divisão: " + str(divisao))
print("Raiz: " + str(raiz))