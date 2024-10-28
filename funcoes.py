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
                continue
            else:
                break
                
            if afundado:
                navios_afundados += 1
    
    return navios_afundados
            
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    for linha, coluna in posicoes_navio:
        if linha < 0 or linha >= 10 or coluna < 0 or coluna >= 10:
            return False
        
    for navio, lista_posicoes in frota.items():
        for posicoes in lista_posicoes:
            for pos in posicoes:
                if pos in posicoes_navio:
                    return False

    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto