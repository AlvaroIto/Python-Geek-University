# Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura. Crie os métodos
# públicos necessários para sets e gets e também um método para imprimir os dados de uma pessoa







class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = input('Digite o nome: ')
        self.__idade = idade
        self.__altura = altura




    def dados(self):
        return f'Nome: {self.__nome}, Idade: {self.__idade}, Altura: {self.__altura} mts'

#pessoa1 = Pessoa('Alvaro', 34, 1.70)


#print(pessoa1.dados())

print(Pessoa)