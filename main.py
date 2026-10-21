from Mod.inicio import inserir_dados
from Class.cadastrar_lista import Cadastrar_Lista
from pathlib import Path
import os
import time

Time = time

while True:
    
    print("\n-----1: Cadastrar Produtos no Excel.-----")
    print("\n-----2: Inserir uma lista de dados(txt) no Excel-----")
    print("\n-----3: Limpar prompt de comando-----")
    print("\n-----4: Inserir uma lista de dados(JSON)-----")
    print("\n-----5: Sair-----")
    
    try:
        
        opcao = int(input("Digite uma opação: "))
        
        match opcao:
            case 1:
                inserir = inserir_dados()
                print(inserir)
            case 2:
                op = input("caminho definido ou digitar/colar um caminho ?:(c/d) ")
                if op == "d" or op == "D":
                    caminho = input("Digite um caminho")
                    dados = Path(caminho)
                elif op == "c" or op == "C":
                    dados = Path("Data/produtos_500_registros.txt")
                    cadastrar = Cadastrar_Lista()
                    cadastrar.cadastrar(dados)
                else:
                    print("Opção inválida!!")
            case 3:
                os.system("cls")
            case 4:
                print("Opção indisponivel no momento!")
                time.sleep(3)
                os.system("cls")
            case 5:
                op = input("Deseja sair ?(s/n) ")
                if op == "s" or op == "S":
                    print("Obrigado por usar nosso sistema. ;)")
                    time.sleep(3)
                    os.system("cls")
                    break    
            case _:
                print("Digite apenas núneros apresentados como opção!!")
        
    except ValueError as error:
        # error = "Digite uma opção! >:("
        Time.sleep(2)
        print("Digite uma opção...")
        Time.sleep(4)
