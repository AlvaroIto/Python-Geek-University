'''
Orientação a objeto -> mapeamento de objetos do mundo real para modelos computacionais

- Classe -> (objeto do mundo real sendo representado computacionalmente)
- Atributos -> Características do objeto
- Métodos -> Comportamento do objeto. (Métodos são como funções, a diferença é que métodos estão dentro de uma Classe)
- Construtor -> Também é um método. mas serve para criar os objetos a partir da Classe
- Objeto/Instâncias -> São instâncias da classe, ou seja, após mapeamento do objeto no mundo real para sua representação
computacional, podemos criar quantos objetos forem necessários.

Todas classes possuem atributos e métodos
- Atributos: Caracteristicas do objeto (ex.: controle remoto: tamanho, cor, largura....) ( são coisas fixas)
- Métodos: O que a classe faz ( ex.: controle remoto: aumentar e diminuir volume, trocar de canal, voltar...)
  (normalmente os métodos são verbos o que vai fazer)


class Usuario:
                    ########################
                    ## ATRIBUTO DE CLASSE ##
                    ########################
    contador = 0
                    ######################
                    ## MÉTODO DE CLASSE ##
                    ######################
    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

                    ##########################
                    ## ATRIBUTO DE INSTÂCIA ##
                    ##########################                      #########################
    def __init__(self, nome, sobrenome, email, senha):              ## __init__ CONSTRUTOR ##
        self.__id = Usuario.contador + 1                            #########################
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.__id

                    #########################
                    ## MÉTODO DE INSTÂNCIA ##
                    #########################
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

# Objeto/Instâncias
user = Usuario('Felicity', 'Jones', 'felicity@gmail.con', '123456')

Usuario.conta_usuarios()

'''

email = 'alvaro.ito @gmail.com'
servidor = email.split('@')

print(servidor[1])
