class SuperForca:
    def __init__(self):
        self.forca = 0

class Voar:
    def __init__(self):
        self.altitude = 0
    
    def set_altitude(self, nova_altitude):
        self.altitude = nova_altitude
   
class Pessoa:
    def __init__(self):
        self.nome = ""
        self.peso = 0
        self.altura = 0

class IronMan(Pessoa, SuperForca, Voar):
    def __init__(self):
        Pessoa.__init__(self)
        SuperForca.__init__(self)
        Voar.__init__(self)
        self.armadura_ativada = False
    
    def set_altitude(self, nova_altitude):
        if self.armadura_ativada:
            self.altitude = nova_altitude
            return
        print("Voe somente com a armadura ativada")
    
    def jarvis(self):
        if self.armadura_ativada:
            self.set_altitude(0)
            print("Pousei")
        self.armadura_ativada = not self.armadura_ativada


class Hulk(Pessoa, SuperForca):
    def __init__(self):
        Pessoa.__init__(self)
        SuperForca.__init__(self)
        self.nome = "Bruce Banner"
    
    def ficar_nervoso(self):
        self.forca = 10000000
    
    def vai_pescar(self):
        self.forca = 0
    
