'''
    Calcule e exiba o valor de P, onde x, a e N são informados
    pelo usuário, sendo N o número de termos da sequência:

    P = ax¹ + ax² + ax³ + ...
'''

a = int(input('Informe o valor de a: '))
x = int(input('Informe o valor de x: '))
n = int(input('Informe o valor de n: '))

sequencia = []

for i in range(1, (n + 1)):
    termo = a * (x ** i)
    sequencia.append(termo)

print('Sequência: ' + str(sequencia))

p = sum(sequencia)
print('P: ' + str(p))