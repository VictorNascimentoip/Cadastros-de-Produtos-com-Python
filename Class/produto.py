class ProdutoInvalidoError(Exception):
    """Exceção para dados ívalidos do produto."""
    pass

class Produto:
    
    def __init__(self, idd: int, produto: str, quantidade: int, preco: float):
        
        if idd <= 0:
            raise ProdutoInvalidoError("ID ínvalido!.")
        
        if not produto.strip():
            raise ProdutoInvalidoError("Nome do produto ínvalido.")
        
        if quantidade < 0:
            raise ProdutoInvalidoError("Quantidade ínvalida.")
        
        if preco < 0.0:
            raise ProdutoInvalidoError("Preço ínvalido.")
        
        self.ID = idd
        self.Produto = produto
        self.Quantidade = quantidade
        self.Preco = preco