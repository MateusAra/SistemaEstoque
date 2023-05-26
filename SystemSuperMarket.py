# Classe para representar um produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Classe para representar o carrinho de compras
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

# Função principal do programa
def main():
    carrinho = CarrinhoDeCompras()

    while True:
        print("1 - Adicionar produto")
        print("2 - Calcular total")
        print("3 - Finalizar compra")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            produto = Produto(nome, preco)
            carrinho.adicionar_produto(produto)
            print("Produto adicionado ao carrinho!")

        elif opcao == "2":
            total = carrinho.calcular_total()
            print(f"Total: R$ {total:.2f}")

        elif opcao == "3":
            total = carrinho.calcular_total()
            print(f"Total da compra: R$ {total:.2f}")
            print("Compra finalizada!")
            break

        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    # Escrever os produtos do carrinho em um arquivo de texto
    with open("compra.txt", "w") as arquivo:
        for produto in carrinho.produtos:
            arquivo.write(f"{produto.nome}, {produto.preco}\n")

if __name__ == "__main__":
    main()
