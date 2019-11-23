class Veiculo:
    motor = ""
    placa = ""
    modelo = ""
    fabricante = ""
    numero_rodas = 0
    
    def __init__(self):
        self.motor = "Motor novo"
        self.numero_rodas = 4
        
    def set_placa(self, placa):
        self.placa = placa

    def set_numero_rodas(self, rodas):
        self.numero_rodas = rodas

class Moto(Veiculo):
    def __init__(self):
        super().__init__()
        self.numero_rodas = 2

class Caminhao(Veiculo):
    carga_maxima = 0

class Carro(Veiculo):
    pass
    