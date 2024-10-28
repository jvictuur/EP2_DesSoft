from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

navios_info = [
    {"nome": "porta-aviões", "tamanho": 4, "quantidade": 1},
    {"nome": "navio-tanque", "tamanho": 3, "quantidade": 2},
    {"nome": "contratorpedeiro", "tamanho": 2, "quantidade": 3},
    {"nome": "submarino", "tamanho": 1, "quantidade": 4}
]

i = 0
while i < len(navios_info):
    navio = navios_info[i]
    j = 0
    
    while j < navio["quantidade"]:
        print(f"Insira as informações referentes ao navio {navio['nome']} que possui tamanho {navio['tamanho']}")
        
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
    
        if navio["nome"] == "submarino":
            orientacao_str = "vertical"
        else:
            orientacao = int(input("[1] Vertical [2] Horizontal > "))
            orientacao_str = "vertical" if orientacao == 1 else "horizontal"
        
        if posicao_valida(frota, linha, coluna, orientacao_str, navio["tamanho"]):
            define_posicoes(linha, coluna, orientacao_str, navio["tamanho"])
            frota = preenche_frota(frota, navio["nome"], linha, coluna, orientacao_str, navio["tamanho"])
            j += 1  
        else:
            print("Esta posição não está válida!")
    
    i += 1  

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True
posicoes_atacadas = []

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    
    while True:
        linha = int(input("Jogador, qual linha deseja atacar? "))
        if 0 <= linha <= 9:
            break
        print("Linha inválida!")

    while True:
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        if 0 <= coluna <= 9:
            break
        print("Coluna inválida!")

    if (linha, coluna) in posicoes_atacadas:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        continue

    posicoes_atacadas.append((linha, coluna))

    faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == len(frota_oponente):
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False