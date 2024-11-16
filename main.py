#criando funções
"""01 – Escreva um programa em Python que crie uma lista de séries da Netflix. Pode
inventar os nomes das séries (pelo menos 5). Depois, exiba a lista de séries para o
usuário mostrando o número do índice e o nome de cada série da lista. Pergunte ao
usuário qual série ele deseja assistir (o usuário deve escolher pelo número do índice).
Por fim, mostre uma mensagem com o nome da série escolhida a partir do número
informado pelo usuário

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
"""

import tkinter as tk


def principal():
    # Lista de séries
    lista_series = {
        1: "The Office",
        2: "The Boys",
        3: "Stranger Things",
        4: "Breaking Bed",
        5: "Band of Brothers"
    }

    # Função para processar a escolha
    def processar_escolha():
        try:
            escolha = int(entrada.get())  # Obtém o número digitado
            if escolha == 0:  # Encerrar o programa
                resultado.config(text="Encerrando... Até logo!", fg="blue")
                janela.after(2000, janela.destroy)  # Fecha a janela em 2 segundos
            elif escolha not in lista_series:  # Escolha inválida
                resultado.config(text="Não está na lista.", fg="red")
            else:  # Exibe a série escolhida
                resultado.config(
                    text=f"Série escolhida: {lista_series[escolha]}", fg="green"
                )
        except ValueError:  # Entrada inválida
            resultado.config(
                text="Entrada inválida! Por favor, digite um número.", fg="red"
            )

    # Janela principal
    janela = tk.Tk()
    janela.title("Netplix")
    janela.geometry("400x300")

    # Rótulo de título
    titulo = tk.Label(janela, text="Netplix", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    # Rótulo da lista de séries
    texto_series = "\n".join([f"{k}: {v}" for k, v in lista_series.items()])
    rotulo_series = tk.Label(janela, text=texto_series, font=("Arial", 12))
    rotulo_series.pack(pady=10)

    # Caixa de entrada
    entrada = tk.Entry(janela, font=("Arial", 12))
    entrada.pack(pady=10)

    # Botão para confirmar a escolha
    botao = tk.Button(
        janela, text="Escolher Série", font=("Outfit", 15), command=processar_escolha
    )
    botao.pack(pady=10)

    # Rótulo para exibir mensagens
    resultado = tk.Label(janela, text="", font=("Arial", 12))
    resultado.pack(pady=10)

    # Executar o loop principal
    janela.mainloop()


# Chamada da função principal
principal()