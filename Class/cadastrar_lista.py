from Class.lista_dados import Lista_dados
from Class.produto import Produto
from Class.Util import ExcelManager 

class Cadastrar_Lista(ExcelManager):
        
    def cadastrar(self, arquivo):
        
        leitor = Lista_dados(arquivo)
        
        produtos = leitor.Ler_arquivo()
        
        wb, ws = self.abrir_tabela()
        
        linha = self.proxima_linha(ws)
        
        for dados in produtos:
            
            produto = Produto(*dados)
        
            ws.cell(row=linha, column=1).value = produto.ID
            ws.cell(row=linha, column=2).value = produto.Produto
            ws.cell(row=linha, column=3).value = produto.Quantidade
            ws.cell(row=linha, column=4).value = produto.Preco
            
            linha += 1
        
        self.atualizar_tabela(ws, linha -1)
        
        self.salvar(wb)
        
        print(f"{len(produtos)} produtos cadastrados.")