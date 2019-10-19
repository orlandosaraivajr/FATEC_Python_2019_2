class Pessoa:
    def mostra_nome(self):
        print(self.nome)
    
    def mostra_idade(self):
        print(self.idade)
    
    def informa_nome(self, nome):
        self.nome = nome
    
    def informa_idade(self, idade):
        self.idade = idade

    def mostrar(self):
        print(self.__dict__)

pessoa1 = Pessoa()
pessoa1.informa_nome("Orlando Saraiva")
pessoa1.informa_idade(38)

pessoa2 = Pessoa()
pessoa2.informa_nome("Ana")

pessoa1.__dict__
pessoa1.__dict__.keys()
pessoa1.__dict__.values()