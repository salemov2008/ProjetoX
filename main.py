#criando funções
"""01 – Escreva um programa em Python que crie uma lista de séries da Netflix. Pode
inventar os nomes das séries (pelo menos 5). Depois, exiba a lista de séries para o
usuário mostrando o número do índice e o nome de cada série da lista. Pergunte ao
usuário qual série ele deseja assistir (o usuário deve escolher pelo número do índice).
Por fim, mostre uma mensagem com o nome da série escolhida a partir do número
informado pelo usuário"""

def principal():
    print("Netplix")
    lista_series = {1:"The Office", 2:"The Boys", 3:"Stranger Things",
                    4:"Breaking Bed", 5:"Band of Brothers"}
    print(lista_series)
    escolha = 0
    while True:

        try:
            escolha = int(input("Digite o número da série que queira assitir (Para sair digite 0): "))
        except ValueError:
            print("\nxxxxxxxxxxx I N V Á L I D O xxxxxxxxxxxxxxxxx\n"
                        "Digite um que exista no nosso universo, por favor.\n"
                         "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
            continue
        if escolha == 0:
            print("\n______________\n"
                    "Encerrando...\n"
                    "______________\n")
            break
        if escolha not in lista_series:
            print("\nxxxxxxxxxxxxxxx\n"
                  "Não está na lista. \n"
                  "xxxxxxxxxxxxxxx\n")
        else:
            print(  "\n---------------------------------------\n"
                    f"Série escolhida: {lista_series[escolha]}\n"
                    "---------------------------------------\n")

principal()
