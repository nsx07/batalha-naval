from random import randint
navios = ['P','C','F']
CoordenadasX = 20
CoordenadasY = 20
porta_avioes = [3,4]
cruzador = [4,3]
fragata = [5,2]
intervalo = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
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
            id_navio = navios[randint(0,2)]
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
                entrada_X = randint(0,16)
                if entrada_X > 19 or entrada_X < 0:
                    print("Coordenada inexistente. Tente novamente! ")
                    continue
                else: 
                    break 
            while True:#valida coordenada Y:
                entrada_Y = randint(0,16)
                if entrada_Y > 19 or entrada_Y < 0:
                    print("Coordenada inexistente. Tente novamente! ")
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
            if ocupada:#verifica se todas as posições testadas estão ocupadas ou não, se True, pergunta novas coordernadas
                continue
            else:#se não, preenche o tabuleiro
                for pecas in range(quant_Pecas):#preenche o tabuleiro
                    tabuleiro[entrada_X][entrada_Y+pecas] = id_navio             
                break
        visualizar_Tabuleiro()
        quant_avioes -= 1
def tentativa():
    pontuacao = 0
    cont_partesRestantes = 0
    for x in range(CoordenadasX):
        for y in range(CoordenadasY):
            if tabuleiro[x][y] != '0':
                cont_partesRestantes += 1
    while cont_partesRestantes != 0:
        tentativa_X = randint(0,19)
        tentativa_Y = randint(0,19)
        if tabuleiro[tentativa_X][tentativa_Y] != 0:
            if tabuleiro[tentativa_X][tentativa_Y] == 'P':            
                print("PORTA-AVIÃO")
                tabuleiro[tentativa_X][tentativa_Y] = 'X'
                alvo_atingido = True
                # checar 4 indices
                if tentativa_Y == 19:# se o alvo estiver na ultima posição 
                  for y in range(1,4):
                    if tabuleiro[tentativa_X][tentativa_Y-y] == 'X':
                      valida_ponto = True
                    else:
                      valida_ponto = False
                      break
                  if valida_ponto:
                    print('Você naufragou um Porta-Aviões')
                    pontuacao += 30
                elif tentativa_Y == 0:# se o alvo estiver na primeira posição 
                  for y in range(1,4):
                    if tabuleiro[tentativa_X][tentativa_Y+y] == 'X':
                      valida_ponto = True
                    else:
                      valida_ponto = False
                      break
                  if valida_ponto:
                    print('Você naufragou um Porta-Aviões')
                    pontuacao += 30
                else: #validar as 4 possíveis posições do tiro no porta-aviões
                  for y in range(1,4):
                    if tabuleiro[tentativa_X][tentativa_Y-y] == 'X':
                      valida_ponto = True
                    else:
                      valida_ponto = False
                      break
                  if valida_ponto:
                    print('Você naufragou um Porta-Aviões')
                    pontuacao += 30                  
            elif tabuleiro[tentativa_X][tentativa_Y] == 'C':
                print("CRUZADOR")
                tabuleiro[tentativa_X][tentativa_Y] = 'X'
                alvo_atingido = True
                # checar 3 indices
                if tentativa_Y == 19:# se o alvo estiver na ultima posição
                  for y in range(1,3):
                    if tabuleiro[tentativa_X][tentativa_Y-y] == 'X':
                      valida_ponto = True
                    else:
                      valida_ponto = False
                      break
                  if valida_ponto:
                    print('Você naufragou um Cruzador')
                    pontuacao += 20
                elif tentativa_Y == 0:# se o alvo estiver na primeira posição
                  for y in range(1,3):
                    if tabuleiro[tentativa_X][tentativa_Y+y] == 'X':
                      valida_ponto = True
                    else:
                      valida_ponto = False
                      break
                  if valida_ponto:
                    print('Você naufragou um Cruzador')
                    pontuacao += 20
                #else: validar as 3 possíveis posições de tiro no cruzador
            elif tabuleiro[tentativa_X][tentativa_Y] == 'F':
                print("FRAGATA")
                tabuleiro[tentativa_X][tentativa_Y] = 'X'
                alvo_atingido = True
                # checar 2 indices
                if tentativa_Y == 19:# se o alvo estiver na ultima posição 
                  if tabuleiro[tentativa_X][tentativa_Y-1] == 'X':
                    print('Você naufragou uma Fragata')
                    pontuacao += 10
                elif tentativa_Y == 0:# se o alvo estiver na primeira posição
                  if tabuleiro[tentativa_X][tentativa_Y+1] == 'X':
                    print('Você naufragou uma Fragata')
                    pontuacao += 10
                else:
                  if tabuleiro[tentativa_X][tentativa_Y+1] == 'X' or tabuleiro[tentativa_X][tentativa_Y-1] == 'X' :
                    print('Você naufragou uma Fragata')
                    pontuacao += 10                 
            else: 
                print("Parte do návio já atingida")#checar erro quando digita uma localização que não possui nada
                continue
        else:
            print("Nada consta.")
            alvo_atingido = False
            pontuacao -= 1
        
        #sair = input(f"sua pontuação é {pontuacao}.\n se deseja fechar o jogo, digite 0, caso contrário, pressione Enter.")#mecanismo de saida do jogo
        #if sair == "0":
        #  break
        #else:
        if alvo_atingido:
          cont_partesRestantes -= 1
          continue
        else:
            cont_partesRestantes = cont_partesRestantes
            continue
          
    print("Todas as embarcações foram atingidas!")
def main():
    gerador_Tabuleiro()
    posicionar_pecas()
    tentativa()
    visualizar_Tabuleiro()
main()