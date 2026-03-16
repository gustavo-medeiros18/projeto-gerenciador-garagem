# Para pode executar o projeto, primeiro é necessário
# ativar o ambiente virtual, e em seguida instalar
# a biblioteca tabulate, que é utilizada por ele.
# Isso pode ser feito através dos seguintes comandos
# no terminal, que precisa estar aberto na pasta
# do projeto:

# python -m venv .venv
# .\.venv\Scripts\activate
# python -m pip install tabulate

from interfaces.cli import exibir_carros_lista, exibir_carros_tabela, exibir_menu, entrada_cadatrar_carro, entrada_editar_carro, entrada_deletar_carro

while True:
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ").strip()
    print(f"A opção escolhida foi {repr(opcao_escolhida)}")
    if opcao_escolhida == "1":
        entrada_cadatrar_carro()
    elif opcao_escolhida == "2":
        exibir_carros_lista()
    elif opcao_escolhida == "3":
        exibir_carros_tabela()
    elif opcao_escolhida == "4":
        entrada_editar_carro()
    elif opcao_escolhida == "5":
        entrada_deletar_carro()
    elif opcao_escolhida == "6":
        print("\nEncerrando o gerenciador de garagem. Até mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente")