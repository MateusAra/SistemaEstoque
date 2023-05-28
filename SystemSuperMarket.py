from produto import Produto
from carrinho import CarrinhoDeCompras
# Função principal do programa
def main():
    carrinho = CarrinhoDeCompras()

    while True:
        print("\n1 - Adicionar produto")
        print("2 - Ver carrinho")
        print("3 - Calcular total")
        print("4 - Finalizar compra")
        print("5 - Remover um produto")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            try:
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))

                if nome == "" or nome is None:
                    print("\nNome não pode ser vazio.")
                elif preco == 0.00 or preco is None:
                    print("\nPreço não pode ser igual a zero.")
                else:
                    produto = Produto(nome, preco)
                    carrinho.Adicionar_produto(produto)
                    print("\nProduto adicionado ao carrinho!")

            except ValueError:
                print("\nNome ou preço inválido, verifique!")

        elif opcao == "2":
            carrinho.Ver_Carrinho()
            
        elif opcao == "3":
            total = carrinho.Calcular_total()
            if total != None:
                print(f"Total: R$ {total:.2f}")

        elif opcao == "4":
            total = carrinho.Calcular_total()
            if total != None:
                print(f"Total da compra: R$ {total:.2f}")
                print("Compra finalizada!")
                break

        elif opcao == "5":
            nome_Produto = input("Digite o nome do produto que deseja remover: ")
            carrinho.Remover_Produto(nome_Produto)

        elif opcao == "6":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    # Escrever os produtos do carrinho em um arquivo de texto
    with open("Extrato.txt", "w") as arquivo:
        for produto in carrinho.produtos:
            arquivo.write(f"{produto.nome.upper()}........R$ {produto.preco}\n")

if __name__ == "__main__":
    main()
