"""pip install pytest ou cria requirements com as dependencia e coloca o pytest la

Importante o nome das funcoes de teste deve comecar com test_ obrigatoriamente"""

from Concessionaria import *


def test_carro_calcula_valor_com_imposto():
    carro = Carro("TFGE345", 2010, 10000, "Gol", "marca")
    assert carro.calcula_valor_com_imposto() == 13500.0


def test_carro_ano():
    carro = Carro("TFGE345", 2010, 10000, "Gol", "marca")
    assert carro.ano == 2010

