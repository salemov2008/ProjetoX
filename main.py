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
            escolha = int(input("Digite o número da série que queira assitir (1 a 5): "))
        except ValueError:
            print("Digite um que exista no nosso universo, por favor.")



    while True:
        if escolha not in lista_series:
            print("Não está na lista.")
        break




principal()
