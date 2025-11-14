class Pessoa:
    # construtor
    def __init__(self, nome, idade, genero, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero 
        self.__telefone = telefone 

    def __str__(self):
        return f"Olá, meu nome é {self.nome}, tenho {len(self)}  anos, sou do gênero {self.__genero} e meu telefone é {self.__telefone}."

    # métodos set e get
    @property 
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property 
    def idade(self):
        return self.__idade

    @nome.setter
    def idade(self, idade):
        self.__idade = idade

    @property 
    def genero(self):
        return self.__genero

    @nome.setter
    def genero(self, genero):
        self.__genero = genero

    @property 
    def telenofe(self):
        return self.__telefone

    @nome.setter
    def telefone(self, telefone):
        self.__genero = telefone