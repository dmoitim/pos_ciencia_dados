'''
    Fibonacci
    O usuário deve informar quantos termos a sequência deve ter
    e o algoritmo armazenar em uma lista e exibi-la ao final
'''

def fibonacci(n):
    fib = []

    anterior1 = 0
    anterior2 = 1

    fib.append(anterior1)
    fib.append(anterior2)

    for i in range(2, n): # Já temos os dois primeiros elementos, por isso começa do 2
        atual = anterior1 + anterior2
        fib.append(atual)

        anterior1 = anterior2
        anterior2 = atual

    print(fib)

n = int(input('Digite a quantidade desejada: '))
fibonacci(n)