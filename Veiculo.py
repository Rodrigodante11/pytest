class Veiculo:
    def __init__(self, placa, ano, valor):  # contrutor
        self.placa = placa
        self.ano = ano
        self.valor = valor

    def calcula_valor_com_imposto(self):
        return self.valor + self.valor * 0.25


class Carro(Veiculo):
    def __init__(self, placa, ano, valor, modelo, marca):  # contrutor
        super().__init__(placa, ano, valor)
        self.modelo = modelo
        self.marca = marca

    # Override
    def calcula_valor_com_imposto(self):
        return super(Carro, self).calcula_valor_com_imposto() + self.valor * 0.1
