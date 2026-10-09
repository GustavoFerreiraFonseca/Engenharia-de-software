# Esse será o meu arquivo de testes.
# 1 - Executar sem o código da calculadora. (Red fase)
# 2 - Executar com o código da calculadora. (Green Fase)
# 3 - Executar com o código da calculadora refatorado. (Refactor fase)

# Passo 1: Testes que serão realizados, um em cada etapa.
#Sem desconto (clientes comuns).
#Desconto percentual fixo (ex: Clientes PREMIUM ganham 10% de desconto).  
#Desconto de valor fixo/cupom (ex: Cupom DESCONTO20 tira R$ 20,00).  

# Escolhi usar o strategy, pois dessa forma será possível saber qual 
# desconto aplicar herdando um unico método da classe mãe.
# darei 5 minutos para a fase 1 (Red), 
#       30 minutos para a fase 2(Green)
#       75 minutos para a fase 3 (Refactor)
#       10 minutos finais para a autoavaliação e enviar o arquivo.

# O tempo é maior devido também a necessidade de eu ter que pesquisar
# na internet, youtube como realizar determinadas coisas em python.

import pytest

from calculadora_desconto import CalculadoraDesconto

def test_cliente_comum_sem_desconto():
    calculadora = CalculadoraDesconto()
    assert calculadora.calcular_total(100.0, tipo_desconto="NENHUM") == 100.0

def test_cliente_vip_desconto_percentual():
    calculadora = CalculadoraDesconto()
    assert calculadora.calcular_total(100.0, tipo_desconto="PREMIUM", percentual=10) == 90.0

def test_cupom_desconto_valor_fixo():
    calculadora = CalculadoraDesconto()
    assert calculadora.calcular_total(100.0, tipo_desconto="CUPOM", valor_cupom=20.0) == 80.0