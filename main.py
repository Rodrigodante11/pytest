from Veiculo import Veiculo, Carro

veiculo = Veiculo("TFGE345", 2010, 10000)

print(veiculo.calcula_valor_com_imposto())

carro = Carro("TFGE345", 2010, 10000, "Gol", "marca")
print(carro.calcula_valor_com_imposto())

