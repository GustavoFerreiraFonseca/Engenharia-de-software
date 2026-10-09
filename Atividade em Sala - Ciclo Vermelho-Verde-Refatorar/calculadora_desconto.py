# Atividade A1 parte 3.
# Aluno: Gustavo Ferreira da Fonseca, RA: 2669510
# Aplicação das três fases do TDD:
#     Vermelho-Verde-Refatorar


# Red fase, aqui vamos implementar um padrão de projeto para
# melhorar/refatorar o código que já funciona.

# Escolhi o padrão de projeto Strategy

from abc import ABC, abstractmethod

class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class DescontoNenhum(EstrategiaDesconto):
    def calcular(self, valor: float) -> float:
        return valor

class DescontoPercentual(EstrategiaDesconto):
    def __init__(self, porcentagem: float):
        self.porcentagem = porcentagem

    def calcular(self, valor: float) -> float:
        return valor * (1 - self.porcentagem / 100)

class DescontoFixo(EstrategiaDesconto):
    def __init__(self, valor_desconto: float):
        self.valor_desconto = valor_desconto

    def calcular(self, valor: float) -> float:
        return max(0.0, valor - self.valor_desconto)

class CalculadoraPreco:
    def __init__(self, estrategia: EstrategiaDesconto):
        self.estrategia = estrategia

    def calcular_total(self, valor: float) -> float:
        return self.estrategia.calcular(valor)
        
# Autoavaliação:

# Executei o suite novamente e atingi todos os critérios. Comitei duas vezes a fase vermelha
#, pois a primeira vez enviei sem os casos de teste, mas já arrumei.
# A diferença da fase verde para a refatorada é apenas o uso de um
# padrão de projeto chamado strategy.

# Ademais, gostei muito dessa prática, foi bem útil não só para fixar
# os conteúdos vistos, mas também para aprender mais de python.

#Gustao Ferreira da Fonseca, RA 2669510
