from Class.cadastrar_dados import Cadastrar_Dados
from Class.produto import ProdutoInvalidoError
from Class.produto import Produto


def inserir_dados():
    
    menssagem = "Retornando ao loop!"
    
    try:
    
        idd = int(input("Digite um ID: "))
        produto = input("Digite um Produto: ")
        quantidade = int(input("Digite uma Quantidade: "))
        preco = float(input("Digite um preco: "))
    
        produtos = Produto(
            idd,
            produto,
            quantidade,
            preco
        ) 
    
        cadastro = Cadastrar_Dados()
    
        if cadastro.cadastrar(produtos):
    
            print("\nProduto cadastrado com suceso!")
    
    except ValueError:
        print("ID, Quantidade e Preço devem se númericos")
    
    except ProdutoInvalidoError as erro:
        print(erro)
    
    except FileNotFoundError:
        print("Arquivo não encontrado")
    
    return menssagem
    
    