def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes_nav = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio in frota:
        frota[nome_navio].append(posicoes_nav)
    else:
        frota[nome_navio] = [posicoes_nav]
    
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X' 
    else:
        tabuleiro[linha][coluna] = '-' 

    return tabuleiro

def posiciona_frota(frota):
    tamanho_tabuleiro = 10
    tabuleiro = [[0 for _ in range(tamanho_tabuleiro)] for _ in range(tamanho_tabuleiro)]

    for navio, lista_posicoes in frota.items():
        for posicoes in lista_posicoes:
            for pos in posicoes:
                linha, coluna = pos
                tabuleiro[linha][coluna] = 1  

    return tabuleiro
