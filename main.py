from Concessionaria import Veiculo, Carro, Concessionaria

veiculo = Veiculo("TFGE345", 2010, 10000)

print(veiculo.calcula_valor_com_imposto())

carroaa = Carro("TFGE345", 2010, 10000, "Gol", "marca")
print(carroaa.calcula_valor_com_imposto())

concessionaria = Concessionaria("ConceAB", "Santa Rita", carroaa)
print(concessionaria.carro.placa)

