'''

Classe:

Podem conter:
    - Atributos -> (características do objeto), podemos representar os estados de um objeto. Por exemplo da lâmpada,
      podemos saber a voltagem, cor, luminosidade...

    - Métodos -> Representam os comportamentos do objeto, ou seja, as açoes que este objeto pode fazer. Por exemplo da
      lâmpada comportamento de ligar e desligar

class Lampada:
    pass

lamp = Lampada()
print(type(lamp))


Atributos:

Dividos em 3 grupos:
    - Atributos de Instânca
    - Atributos de Classe
    - Atrbutos Dinâmicos

OBS.: Todo atributo de uma classe é público, ou seja, pode ser acessado em todo projeto.
Caso queiramos demosntrar que determinad atributo deve ser tratado como privado, ou seja, utilizar somente dentro da
própria classe, utiliza-se o __ duplo underscore no início de seu nome

#Classe com atributo de instancia publico
class Lampada:
    #métodos
    def __init__(self, voltagem, cor):
        #atributos de instância
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

#Classe com atributo de instancia privados
class Lampada:
    #métodos
    def __init__(self, voltagem, cor):
        #atributos de instância
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


- INSTÂNCIA -> atributos declarados dentro do método construtor
( ao criar instância/objetos de uma classe, todas as instâncias terão estes atributos)
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.email)
user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()


- CLASSE -> atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente ja inicializamos
 um valor, este valor é compartilhado entre todas as instancas da classe
class Produto:
    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)

p1 = Produto('Playstation 4', 'video game', 2300)
p2 = Produto('Xbox S', 'video game', 4500)

print(p1.valor)
print(p2.valor)
print(Produto.imposto) # Acesso de um atributo de classe


- DINÂMICOS -> atributos de instância que são criados em tempo de execução. sendo exclusivo da instância que o criou
class Produto:
    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 4500)

#Criando um atributo dinâmco em tempo de execução
p2.peso = '5kg'

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

'''


