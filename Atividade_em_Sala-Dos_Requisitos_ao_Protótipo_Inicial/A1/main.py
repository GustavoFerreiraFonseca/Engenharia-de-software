# Código referente a A1, parte 2.
# Gustavo Ferreira da Fonseca, RA: 2669510
# Planejamento:
#    1. Ler atentamente a A1 parte 1.
#    2. Escolher de 1 a 3 requisitos.
#    3. Aprender o necessário na linguagem python para implementá-los.
#    4. Elaborar um planjamento para programar o requisito.   
#    5. Iniciar a sua implementação em arquivos separados.
#    
#    
#    --> Requisitos escolhidos para iniciar a implementação:
#       
#           1. "Como usuário eu quero saber quais vagas estão disponíveis em tempo real do campus"
#    
#    --> Planejamento:       
#           
#           1. Desenvolver uma classe chamada Vaga:
#               
#               1.1. Ela conterá as seguintes atributos e métodos iniciais:
#               
#                   1.1.1. Disponivel
#                   1.1.2. Construtor, Destrutor, getters, setters e listar
#           
#           
#           2. Desenvolver um menu para o usuário com as seguintes opções:
#               
#               1.1. Listar vagas disponíveis
#               1.2. Sair do aplicativo
#                
#  

from requisito1 import *

# Menu do usuário
while True:
    
    print("-_-_- Menu do Usuário -_-_-\n")
    print("1 - Listar vagas disponíveis!\n")
    print("2 - Sair do aplicativo!\n")
    
    opcao = int(input("Escolha uma opção:"))
    
    match opcao:
        case 1:
            # Chamo o metodo listar do meu objeto de Vaga
            continue
        
        case 2: 
            break
        case _:
            print("Você digitou um valor incorreto!\n");
            continue    
        