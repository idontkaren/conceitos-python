
def usuario_escolhe_jogada(n, m):

    jogadaValida = False
       
    while not jogadaValida:
        jogadorRetira = int(input("Quantas peças você vai tirar? "))
        
        if jogadorRetira > m or jogadorRetira < 1:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            jogadaValida = True
    
    return jogadorRetira

def computador_escolhe_jogada(n, m):
    computadorRetira = 1
    
    while computadorRetira < m:
        if (n - computadorRetira) % (m + 1) == 0:
            return computadorRetira
        else:
            computadorRetira += 1
    
    return computadorRetira

def partida():
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print()
        print("Você começa!")
        print()
        jogador = True
    else:
        print()
        print("Computador começa!")
        print()
        jogador = False
    
    while n > 0:
        if jogador:
            qtdRetirada = usuario_escolhe_jogada(n, m)
            n = n - qtdRetirada
            jogador = False
            if qtdRetirada == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou ", qtdRetirada, "peças.")
        else:
            qtdRetirada = computador_escolhe_jogada(n, m)
            n = n - qtdRetirada
            jogador = True
            if qtdRetirada == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou ", qtdRetirada, "peças.")
        if n == 1:
            print("Agora resta uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print("Agora restam", n, "peças no tabuleiro.")
                print()
            else:
                print("Fim do jogo! O computador ganhou!")
                print()

def campeonato():
    contador = 1
    while contador <= 3:
        print("*** Rodada ", contador, " ****")
        print()
        partida()
        contador +=1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")    
    
print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato"))
if escolha == 2:
    print("Voce escolheu um campeonato!")
    print()
    campeonato()
else:
    partida()