"""pip install pytest ou cria requirements com as dependencia e coloca o pytest la

Importante o nome das funcoes de teste deve comecar com test_ obrigatoriamente"""
import pytest

from Veiculo import *
from unittest import mock


def test_calcula_valor_com_imposto():
    veiculo = Veiculo("TFGE345", 2010, 10000)
    assert veiculo.calcula_valor_com_imposto() == 12500.0


def test_calcula_valor_com_imposto_value_error():
    with pytest.raises(TypeError):
        veiculo = Veiculo("TFGE345", 2010, "50000")
        result = veiculo.calcula_valor_com_imposto()


def test_carro_calcula_valor_com_imposto():
    carro = Carro("TFGE345", 2010, 10000, "Gol", "marca")
    assert carro.calcula_valor_com_imposto() == 13500.0


def test_carro_ano():
    carro = Carro("TFGE345", 2010, 10000, "Gol", "marca")
    assert carro.ano == 2010


def test_veiculo():
    carro = mock.Mock()
    concessionaria = Concessionaria("ConceAB", "Santa Rita", carro)
    assert concessionaria.nome == "ConceAB"
