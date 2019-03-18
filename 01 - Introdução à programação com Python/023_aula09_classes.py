'''
Classes

Representa entidades em objetos, cada objeto possui seus
atributos e métodos
'''

class Cachorro():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.idade = idade (um underline - indica que não deve ser acessado de fora (privado), mas permite acessar)
        # self.__idade = idade (dois underlines - força que não deve ser acessado de fora (privado))

    def sentar(self):
        print(self.nome.title() + ' está sentado(a).')

    def rolar(self):
        print(self.nome.title() + ' está rolando.')

juma = Cachorro('Juma', 13)
juma.sentar()
juma.rolar()
print('Juma tem ' + str(juma.idade) + ' anos.')

tininha = Cachorro('Tininha', 4)
tininha.sentar()
tininha.rolar()