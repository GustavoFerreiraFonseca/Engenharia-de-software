# Atividade A1 parte 3.
# Aluno: Gustavo Ferreira da Fonseca, RA: 2669510
# Aplicação das três fases do TDD:
#     Vermelho-Verde-Refatorar

# Green fase - Código já funcional, que roda os testes.

class CalculadoraDesconto:
    def calcular_total(self, valor: float, tipo_desconto: str = "NENHUM", percentual: float = 0.0, valor_cupom: float = 0.0) -> float:
        if tipo_desconto == "PREMIUM":
            return valor * (1 - percentual / 100)
        elif tipo_desconto == "CUPOM":
            return max(0.0, valor - valor_cupom)
        else:
            return valor
