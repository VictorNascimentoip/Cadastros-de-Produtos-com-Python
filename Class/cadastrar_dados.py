from Class.Util import ExcelManager

class Cadastrar_Dados(ExcelManager):
        
    def cadastrar(self, produto):
        
        wb, ws = self.abrir_tabela()
        
        linha = self.proxima_linha(ws)
            
        ws.cell(row=linha, column=1).value = produto.ID
        ws.cell(row=linha, column=2).value = produto.Produto
        ws.cell(row=linha, column=3).value = produto.Quantidade
        ws.cell(row=linha, column=4).value = produto.Preco
        
        self.atualizar_tabela(ws, linha)
        
        self.salvar(wb)
        
        return True