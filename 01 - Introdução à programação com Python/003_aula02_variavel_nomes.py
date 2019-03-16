'''
    começar com letras
    podem conter letras, números e underline
    não podem conter espaços
    não podem ser palavras reservadas
    não são tipadas
'''

# Concatenação
num1 = 10
print("Valor de num1: " + str(num1))

num2 = 20
print("Valor de num2: " + str(num2))

# String
nome = "Python"
print(nome)

# Métodos
print(nome.upper())
print(nome.lower())

# Quebra de linha
print("\n" + nome.upper())

# Tabulação
print("\t" + nome.lower())

# Sem saltar linha
print("sem ", end="")
print("saltar ", end="")
print("linha", end="")

# Números inteiros
a = 10
b = 2
c = 5
d = a + b * c + a

print("\n")
print(d)

# Precedências
# 1- Parênteses
# 2- Multipicação e divisão
# 3- Adição e subtração

# Números pontos flutuantes
a = 1.2
b = 2.6
c = a * b
print(c)