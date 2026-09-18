# Classe Vaga

class Vaga:
    
    vagas = []
    
    def __init__(self, disponivel):      
        self.disponivel = disponivel
        print("Vaga adicionada à listagem!\n")
        
    def __del__(self):
        print("Vaga excluída da listagem!\n")
        
    def listar(self):
        # Listaremos todas as vagas aqui
        print("Listagem de vagas disponíveis!\n")
    
    def getterDisponivel(self):
        return self.disponivel
    
    def setterDisponivel(self, disponivel):
        self.disponivel = disponivel
        
        
        
# Autoavaliação: 
#   1. Consegui ler e aprender um pouco da linguagem.
#   2. Consegui começar a desenvolver a classe vaga.
#   3. Acabou surgindo diversos erros e tive que deletar algumas coisas e começar de novo.
#   4. Dessa forma, não completei o requisito 1 ainda.

        