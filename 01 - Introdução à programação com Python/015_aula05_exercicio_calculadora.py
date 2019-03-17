'''
    Caculadora:
    Recebe dois números (inteiros ou decimais) digitados pelo usuário
    e realiza a soma, subtração, multiplicação e divisão de ambos,
    permitindo a seleção da operação
    e exibe o resultado na tela
'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite a operação (1) Soma - (2) Subtração - (3) Multipicação - (4) Divisão: "))

if operacao == 1:
    resultado = num1 + num2
elif operacao == 2:
    resultado = num1 - num2
elif operacao == 3:
    resultado = num1 * num2
else:
    if num2 == 0:
        resultado = "Impossível realizar divisão por 0."
    else:
        resultado = num1 / num2

print("resultado: " + str(resultado))