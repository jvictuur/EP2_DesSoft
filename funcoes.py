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

def afundados(frota, tabuleiro):
    navios_afundados = 0

    for navio, lista_posicoes in frota.items():
        for posicoes in lista_posicoes:
            afundado = True
            for linha, coluna in posicoes:
                if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro[0]):
                    afundado = False
                    break
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            
            if afundado:
                navios_afundados += 1
    
    return navios_afundados
            


