def exibir_tabuleiro(tabuleiro):
    print("-------------")
    for linha in tabuleiro:
        print("|", end=" ")
        for celula in linha:
            print(celula, end=" | ")
        print("\n-------------")

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[i][coluna] == jogador for i in range(3)):
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogo_acabou = False

    while not jogo_acabou:
        exibir_tabuleiro(tabuleiro)
        linha = int(input("Informe o número da linha (0-2): "))
        coluna = int(input("Informe o número da coluna (0-2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print("Jogador", jogador_atual, "venceu!")
            jogo_acabou = True
        elif all(celula != " " for linha in tabuleiro for celula in linha):
            exibir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            jogo_acabou = True
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"

jogar()
