'''
- Métodos (funções) -> Representam os comportamentos do objeto, ou seja, as ações qu este objeto pode realizar

O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da
classe
Todo elemento que inicia e finaliza com duplo underline é chamado de dunder (double underline)

Qual método utilizar?!

Dividos em 2 grupos:
    - Métodos de instância
        Utilizar quando necessitar acessar os atributos de instância
    - Métodos de Classe
        Utilizar quando não é necessário acessar atributos de instância

        - INSTÂNCIA:

        class Lampada:

            def __init__(self, cor, voltagem, luminosidade):
                self.__cor = cor
                self.__voltagem = voltagem
                self.__luminosidade = luminosidade
                self.__ligada = False

        class ContaCorrente:

            contador = 4999

            def __init__(self, limite, saldo):
                self.__numero = ContaCorrente.contador + 1
                self.__limite = limite
                self.__saldo = saldo
                ContaCorrente.contador = self.__numero

        class Produto:

            contador = 0

            def __init__(self, nome, descricao, valor):
                self.__id = Produto.contador + 1
                self.__nome = nome
                self.__descricao = descricao
                self.__valor = valor
                Produto.contador = self.__id

            #Método de instância
            def desconto(self, porcentagem):
                """Retorna o valor do produto com desconto"""
                return (self.__valor * (100 - porcentagem)) / 100

        class Usuario:

            def __init__(self, nome, sobrenome, email, senha):
                self.__nome = nome
                self.__sobrenome = sobrenome
                self.__email = email
                self.__senha = senha

            #Método de instância
            def nome_completo(self):
                return f'{self.__nome} {self.__sobrenome}'


        p1 = Produto('Playstation', 'Video Game', 2300)
        print(p1.desconto(50))

        user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '12346')
        user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')
        print(user1.nome_completo())
        print(user2.nome_completo())


        - CLASSE
        class Usuario:

            contador = 0

            # Método de classe
            @classmethod
            def conta_usuarios(cls):
                print(f'Temos {cls.contador} usuários no sistema')

            # Méto de instância
            def __init__(self, nome, sobrenome, email, senha):
                self.__id = Usuario.contador + 1
                self.__nome = nome
                self.__sobrenome = sobrenome
                self.__email = email
                self.__senha = senha
                Usuario.contador = self.__id

            def nome_completo(self):
                return f'{self.__nome} {self.__sobrenome}'

        user = Usuario('Felicity', 'Jones', 'felicity@gmail.con', '123456')

        Usuario.conta_usuarios()


'''

