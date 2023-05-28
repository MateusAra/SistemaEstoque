# Classe para representar o carrinho de compras
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        if len(self.produtos) == 0:
            print("\nNão há itens no carinho.")
        else:
            total = 0
            for produto in self.produtos:
                total += produto.preco
            return total
    def ver_Carrinho(self):
        if len(self.produtos) == 0:
            print("\nNão há itens no carinho.")
        else:
            for produto in self.produtos:
                print(f"{produto.nome.upper()}......R$ {produto.preco}")