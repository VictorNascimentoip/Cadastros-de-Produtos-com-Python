
import json

class Lista_dados:
    def __init__(self, arquivo: str):
        self.Arquivo = arquivo
        
    def Ler_arquivo(self):
        
        produtos = []
        
        with open(self.Arquivo, "r", encoding="utf-8") as arquivo:
            
            for linha in arquivo:
                   
                dados = linha.strip().split(",")
                
                if len(dados) != 4:
                    continue
                
                try:
                    
                    idd = int(dados[0])
                    nome = dados[1]
                    quantidade = int(dados[2])
                    preco = float(dados[3])
                    
                    produtos.append(
                        (idd, nome, quantidade, preco)
                    )
                    
                except ValueError:
                    
                    print(f"Registro inválido!: {linha}")
        
        return produtos
    
    # Em manutenção
    def ler_arquivo_json(self):
        
        # produtos = []
        
        # with open(self.Arquivo, "r", encoding="utf-8") as arquivo:
        #     dados = json.load(arquivo)
            
        #     for linha in arquivo:
                
        #         dados = linha.strip().split(",")
                
        #         if len(dados) != 4:
        #             continue
                
        #         try:
                    
        #             idd = int(dados[0])
        #             nome = dados[1]
        #             quantidade = int(dados[2])
        #             preco = float(dados[3])
                    
        #             produtos.append(
        #                 (idd, nome, quantidade, preco)
        #             )
                
        #         except ValueError:
                    
        #             print(f"{linha}")
        
        return ""