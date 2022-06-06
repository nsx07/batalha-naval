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
    quant_avioes = 12
    cont_portaAvioes = 0
    cont_cruzador = 0
    cont_fragata = 0
    print("Modelos de Navios\n","Porta-Aviões (Você possui 3, e cada uma possui 4 partes)\n","Cruzador (Você possui 4, e cada um possui 3 partes)\n","Fragata (Você possui 5 e cada um possui 2 partes)\n")
    while quant_avioes > 0:
        print("Identificação das embarcações \n","P - Porta-Aviões.\n","C - Cruzador.\n","F - Fragata.\n")
        while True:#recebe e valida o tipo da embarcação
            id_navio = input("Dê a identificação do návio: ")
            if id_navio == "P":
                quant_Pecas = porta_avioes[1]
                cont_portaAvioes += 1
                if cont_portaAvioes > porta_avioes[0]:
                    print('Quantidade de Porta Aviões atingida!')
                    continue
                else:
                    break
            elif id_navio == "C":
                quant_Pecas = cruzador[1]
                cont_cruzador += 1
                if cont_cruzador > cruzador[0]:
                    print('Quantidade de Cruzador atingida!')
                    continue
                else:
                    break
            elif id_navio == "F":
                quant_Pecas = fragata[1]
                cont_fragata += 1
                if cont_fragata > fragata[0]:
                    print('Quantidade de Fragata atinigda!')
                    continue
                else:
                    break
            else:
                print("Modelo inexistente. Tente novamente! ")
                continue
        limiteY = 20 - quant_Pecas
        print("ATENÇÃO!!")
        print(f"Os valores de X variam de 0 até 19, e os de Y variam de 0 até {limiteY}")
        while True:#pergunta as coordenadas, preenche a matriz e valida os dados 
            while True:#valida coordenada X
                entrada_X = int(input("Dê as coordenadas de X que gostaria de dispor a peça: "))
                if entrada_X > 19 or entrada_X < 0:
                    print("Coordenada inexistente. Tente novamente! ")
                    continue
                else:
                    break
            while True:#valida coordenada Y:
                entrada_Y = int(input("Dê as coordenadas de Y que gostaria de dispor a peça: "))
                if entrada_Y > limiteY or entrada_Y < 0:
                    print("Coordenada inexistente.Tente novamente! ")
                    continue
                else:
                    break            
            for verifica in range(quant_Pecas):#testa se as coordenadas estão livres
                if tabuleiro[entrada_X][entrada_Y+verifica] != 0:
                    print(f"Posição [{entrada_X}][{entrada_Y+verifica}] já ocupada por outra embarcação. Tente outra!")
                    ocupada = True
                    break
                else: 
                    ocupada = False
            if ocupada:
                continue
            else:     
                for pecas in range(quant_Pecas):#preenche o tabuleiro
                    tabuleiro[entrada_X][entrada_Y+pecas] = id_navio             
                break
        visualizar_Tabuleiro()
        quant_avioes -= 1
def tentativa():#debugar e afinar o code
    cont_partesRestantes = 0
    for x in range(CoordenadasX):
        for y in range(CoordenadasY):
            if tabuleiro[x][y] != '0':
                cont_partesRestantes += 1
    while cont_partesRestantes != 0:
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
        if tabuleiro[tentativa_X][tentativa_Y] != '0':
            if tabuleiro[tentativa_X][tentativa_Y] != 'X':            
                print("Tem algo aqui")
                tabuleiro[tentativa_X][tentativa_Y] = 'X'
                alvo_atingido = True
            else: 
                print("Parte do návio já atingida")
                continue
        else:
            print("Nada consta.")
            alvo_atingido = False
        if alvo_atingido:
            cont_partesRestantes -= 1
            continue
        else:
            cont_partesRestantes = cont_partesRestantes
            continue
def main():
    gerador_Tabuleiro()
    posicionar_pecas()
    tentativa()
    visualizar_Tabuleiro()
main()