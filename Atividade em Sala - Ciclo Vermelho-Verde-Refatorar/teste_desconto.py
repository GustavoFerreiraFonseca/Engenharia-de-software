# Esse será o meu arquivo de testes.
# 1 - Executar sem o código da calculadora. (Red fase)
# 2 - Executar com o código da calculadora. (Green Fase)
# 3 - Executar com o código da calculadora refatorado. (Refactor fase)

# Passo 1: Testes que serão realizados, um em cada etapa.
#Sem desconto (clientes comuns).
#Desconto percentual fixo (ex: Clientes PREMIUM ganham 10% de desconto).  
#Desconto de valor fixo/cupom (ex: Cupom DESCONTO20 tira R$ 20,00).  

import pytest
from calculadora_desconto import CalculadoraPreco

def test_cliente_comum_sem_desconto():
    calculadora = CalculadoraPreco()
    assert calculadora.calcular_total(100.0, tipo_desconto="NENHUM") == 100.0

def test_cliente_vip_desconto_percentual():
    calculadora = CalculadoraPreco()
    assert calculadora.calcular_total(100.0, tipo_desconto="PREMIUM", percentual=10) == 90.0

def test_cupom_desconto_valor_fixo():
    calculadora = CalculadoraPreco()
    assert calculadora.calcular_total(100.0, tipo_desconto="CUPOM", valor_cupom=20.0) == 80.0