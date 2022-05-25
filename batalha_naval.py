# batalha naval
from random import randint
CoordenadasX = 20
CoordenadasY = 20
porta_avioes = [3,4]
cruzador = [4,3]
fragata = [5,2]
def gerador_Tabuleiro():
    global tabuleiro
    tabuleiro = [0] * CoordenadasX
    for x in range(CoordenadasX):
        tabuleiro[x] = [0] * CoordenadasY
def visualizar_Tabuleiro():
    for x in range(CoordenadasX):
        print(tabuleiro[x])
def posicionar_pecas():
    while True:
        quant_Pecas = input("Informe o modelo do navio: ")
        if quant_Pecas == "Porta-Aviões":
            quant_Pecas = porta_avioes[1]
            break
        elif quant_Pecas == "Cruzador":
            quant_Pecas = cruzador[1]
            break
        elif quant_Pecas == "Fragata":
            quant_Pecas = fragata[1]
            break
        else:
            print("Modelo inexistente. Tente novamente! ")
            continue
    print("ATENÇÃO!!")
    print(f"Os valores de X variam de 0 até 19, e os de Y variam de 0 até {20 - quant_Pecas}")
    while True:
        entrada_X = int(input("Dê as coordenadas de X que gostaria de dispor a peça. "))
        if entrada_X > 19 or entrada_X < 0:
            print("Coordenada inexistente. Tente novamente! ")
            continue
        else: 
            break
    while True:    
        entrada_Y = int(input("Dê as coordenadas de Y que gostaria de dispor a peça: "))
        if entrada_Y > 19 or entrada_Y < 0:
            print("Coordenada inexistente.Tente novamente! ")
            continue
        else: 
            break
    id = input("Dê a identificação do návio: ")    
    if quant_Pecas > 1:
        for pecas in range(quant_Pecas):
            tabuleiro[entrada_X][entrada_Y+pecas] = id
    else:
        tabuleiro[entrada_X][entrada_Y] = id
def tentativa():
    while True:
        tentativa_X = int(input("Dê a coordenada de X do alvo: "))
        if tentativa_X > 19 or tentativa_X < 0:
            print("Coordenada inexistente. Tente novamente! ")
            continue
        else: 
            break
    while True:
        tentativa_Y = int(input("Dê a coordenada de Y do alvo: "))
        if tentativa_Y > 19 or tentativa_Y < 0:
            print("Coordenada inexistente. Tente novamente! ")
            continue
        else: 
            break
    if tabuleiro[tentativa_X][tentativa_Y] != 0:
        print("Tem algo aqui")
    else:
        print("Nada consta.")
def main():
    gerador_Tabuleiro()
    print("Modelos de Navios\n","Porta-Aviões (Você possui 3, e cada uma possui 4 partes)\n","Cruzador (Você possui 4, e cada um possui 3 partes)\n","Fragata (Você possui 5 e cada um possui 2 partes)\n")
    for navios in range(12):
        posicionar_pecas()
    visualizar_Tabuleiro()
    tentativa()
main()