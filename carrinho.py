
# Classe para representar o carrinho de compras
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def Adicionar_produto(self, produto):
        self.produtos.append(produto)

    def Calcular_total(self):
        if len(self.produtos) == 0:
            print("\nNão há itens no carinho.")
        else:
            total = 0
            for produto in self.produtos:
                total += produto.preco

            cupom = input("Digite seu cupom de desconto caso tenha: ")
            if cupom != None:
                cupom = cupom.split(" ")
                total -= total * (int(cupom[1]) /100) 
            return total
        
    def Ver_Carrinho(self):
        if len(self.produtos) == 0:
            print("\nNão há itens no carinho.")
        else:
            for produto in self.produtos:
                print(f"{produto.nome.upper()}......R$ {produto.preco}")

    def Remover_Produto(self, nome):
        try:
            for produto in self.produtos:
                if produto.nome == nome:
                    self.produtos.remove(produto)
        except ValueError:
            print("Produto não está no carrinho")
