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

print(frota)