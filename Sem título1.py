class Carro:
    placa = ""
    ano = ""
    modelo = ""
    def set_modelo(self, modelo):
        if type(modelo) is type('str'):
            self.modelo = modelo.upper()
        else:
            self.modelo = modelo

    def set_modelo2(self, modelo):
        try:
            self.modelo = modelo.upper()
        except:
            self.modelo = modelo

class Estacionamento:
    vagas = []
    def adicionar_carro(self, carro):
        self.vagas.append(carro)
