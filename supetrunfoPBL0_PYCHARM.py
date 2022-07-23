#/***************************
# Autora: Luana de Melo Fraga
# Componente Curricular: Algoritmos I
# Concluido em: 16/11/2019
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de outro colega
# ou de outro autor, tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da Internet.
# Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte do
# código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# ******************************/#

import random
from os import system
print("Bem vindo ao jogo - Allons-y! ")
#Variáveis
op = 0
contador = 0
recorde = 0
at1 = (int(random.randint(1,10)))
at2 = (int(random.randint(1,10)))
at3 = (int(random.randint(1,10)))
at4 = (int(random.randint(1,10)))
at5 = (int(random.randint(1,10)))
at6 = (int(random.randint(1,10)))
at7 = (int(random.randint(1,10)))
at8 = (int(random.randint(1,10)))
at9 = (int(random.randint(1,10)))
at10 = (int(random.randint(1,10)))
at11 = (int(random.randint(1,10)))
at12 = (int(random.randint(1,10)))
at13 = (int(random.randint(1,10)))
at14 = (int(random.randint(1,10)))
at15 = (int(random.randint(1,10)))
at16 = (int(random.randint(1,10)))
at17 = (int(random.randint(1,10)))
at18 = (int(random.randint(1,10)))
peso1 = (int(random.randint(10,50)))
peso2 = (int(random.randint(10,50)))
peso3 = (int(random.randint(10,50)))
pontos_player1 = 0
pontos_player2 = 0
#"Montros"
nomes_cartas = ('Time Lords', 'Daleks', 'The Silent', 'Cybermen', 'The Ux', 'Midnight Entidy')
#Menu
while op != 3:
    print("""    [ 1 ] Iniciar partida
    [ 2 ] Sobre o jogo
    [ 3 ] Sair do jogo """)
    op = input(">>> Oque deseja fazer? ")
    if op == '1':
#Rodada
        jogador1 = input("Jogador número um digite seu nickname: ")
        jogador2 = input("Jogador número dois digite número seu nickname: ")
        rodadas = int()
        while (rodadas < 3):
            rodadas = int(input(jogador1 + " escolha um número de rodadas MAIOR ou igual três: "))
        while contador < rodadas:
            jogador_da_vez = random.randint(1,2)
            if jogador_da_vez == 1:
                primeiro_jogador = jogador1
                segundo_jogador = jogador2
            elif jogador_da_vez == 2:
                primeiro_jogador = jogador2
                segundo_jogador = jogador1
            print()
            print('Olá ' + primeiro_jogador)
            print("Essas são as suas cartas: ")
            print()
            print(' >>>>>>>>>>>>>>>>>>> ')
            #Carta1
            print(random.choice(nomes_cartas) + '[ a ]')
            print("> %d <"  "[ 1 ] Força: %d " % (peso1, at1))
            print('> %d <'  "[ 2 ] Biologia: %d " % (peso2, at2))
            print('> %d <'  "[ 3 ] Ataque: %d " % (peso3, at3))
            print(' >>>>>>>>>>>>>>>>>>> ')
            print()
            #Carta2
            print()
            print(' >>>>>>>>>>>>>>>>>>> ')
            print(random.choice(nomes_cartas) + '[ b ]')
            print("> %d <"  "[ 1 ] Força: %d " % (peso1, at4))
            print('> %d <'  "[ 2 ] Biologia: %d " % (peso2, at5))
            print('> %d <'  "[ 3 ] Ataque: %d " % (peso3, at6))
            print(' >>>>>>>>>>>>>>>>>>> ')
            print()
            #Carta3
            print()
            print(' >>>>>>>>>>>>>>>>>>> ')
            print(random.choice(nomes_cartas) + '[ c ]')
            print("> %d <"  "[ 1 ] Força: %d " % (peso1, at7))
            print('> %d <'  "[ 2 ] Biologia: %d " % (peso2, at8))
            print('> %d <'  "[ 3 ] Ataque: %d " % (peso3, at9))
            print(' >>>>>>>>>>>>>>>>>>> ')
            print()
            choice = ('')
            atributo_escolhido = ('')
            while (choice != 'a' and choice != 'b' and choice != 'c'):
                choice = input("Você escolhe a carta a, b ou c?: ")
            while (atributo_escolhido != '1' and atributo_escolhido != '2' and atributo_escolhido != '3'):
                atributo_escolhido = input("Você escolhe o atributo 1, 2 ou 3?: ")
            if choice == 'a':
                if atributo_escolhido == "1":
                    atributo = at1
                    pontos = peso1
                elif atributo_escolhido == "2":
                    atributo = at2
                    pontos = peso2
                elif atributo_escolhido == "3":
                    atributo = at3
                    pontos = peso3
            elif choice == 'b':
                if atributo_escolhido == "1":
                    atributo = at4
                    pontos = peso1
                elif atributo_escolhido == "2":
                    atributo = at5
                    pontos = peso2
                elif atributo_escolhido == "3":
                    atributo = at6
                    pontos = peso3
            elif choice == 'c':
                if atributo_escolhido == "1":
                    atributo = at7
                    pontos = peso1
                elif atributo_escolhido == "2":
                    atributo = at8
                    pontos = peso2
                elif atributo_escolhido == "3":
                    atributo = at9
                    pontos = peso3
            print("\n" * 20)
            esta_na_tela = ('')
            while (esta_na_tela != 'sim'):
                esta_na_tela = input(segundo_jogador + ' você ainda está ai? Sim ou não?: ')
            if esta_na_tela == 'sim':
                print()
                print(' >>>>>>>>>>>>>>>>>>> ')
                print("Jogador " + segundo_jogador)
                print("Essas são as suas cartas: ")
                print(' >>>>>>>>>>>>>>>>>>> ')
                print()
                #Carta4
                print()
                print(random.choice(nomes_cartas) + '[ d ]')
                print(' >>>>>>>>>>>>>>>>>>> ')
                print("> %d <"  "[ 1 ] Força: %d " % (peso1, at10))
                print('> %d <'  "[ 2 ] Biologia: %d " % (peso2, at11))
                print('> %d <'  "[ 3 ] Ataque: %d " % (peso3, at12))
                print(' >>>>>>>>>>>>>>>>>>> ')
                print()
                #Carta5
                print()
                print(' >>>>>>>>>>>>>>>>>>> ')
                print(random.choice(nomes_cartas) + '[ e ]')
                print("> %d <"  "[ 1 ] Força: %d " % (peso1, at13))
                print('> %d <'  "[ 2 ] Biologia: %d " % (peso2, at14))
                print('> %d <'  "[ 3 ] Ataque: %d " % (peso3, at15))
                print(' >>>>>>>>>>>>>>>>>>> ')
                print()
                #Carta6
                print()
                print(' >>>>>>>>>>>>>>>>>>> ')
                print(random.choice(nomes_cartas) + '[ f ]')
                print("> %d <"  "[ 1 ] Força: %d " % (peso1, at16))
                print('> %d <'  "[ 2 ] Biologia: %d " % (peso2, at17))
                print('> %d <'  "[ 3 ] Ataque: %d " % (peso3, at18))
                print(' >>>>>>>>>>>>>>>>>>> ')
                print()
                choice2 = ('')
                while (choice2 != 'd' and choice2 != 'e' and choice2 != 'f'):
                    choice2 = input("Você escolhe a carta d, e ou f?: ")
                if choice2 == 'd':
                    if atributo_escolhido == '1':
                        print(' >>>> Atribudo escolhido: Força')
                        atributo2 = at10
                    if atributo_escolhido == '2':
                        print(' >>>> Atribudo escolhido: Biologia')
                        atributo2 = at11
                    if atributo_escolhido == '3':
                        print(' >>>> Atribudo escolhido: Ataque')
                        atributo2 = at12
                elif choice2 == 'e':
                    if atributo_escolhido == '1':
                        print(' >>>> Atribudo escolhido: Força')
                        atributo2 = at13
                    if atributo_escolhido == '2':
                        print(' >>>> Atribudo escolhido: Biologia')
                        atributo2 = at14
                    if atributo_escolhido == '3':
                        print(' >>>> Atribudo escolhido: Ataque')
                        atributo2 = at15
                elif choice2 == 'f':
                    if atributo_escolhido == '1':
                        print(' >>>> Atribudo escolhido: Força')
                        atributo2 = at16
                    if atributo_escolhido == '2':
                        print(' >>>> Atribudo escolhido: Biologia')
                        atributo2 = at17
                    if atributo_escolhido == '3':
                        print(' >>>> Atribudo escolhido: Ataque')
                        atributo2 = at18
                    print('\n' * 10)
                if atributo > atributo2:
                    print()
                    print(">>>>>>> " + primeiro_jogador +" VOCÊ GANHOU!")
                    if primeiro_jogador == jogador1:
                        pontos_player1 = pontos_player1 + pontos
                    elif primeiro_jogador == jogador2:
                        pontos_player2 = pontos_player2 + pontos
                    print('\n' * 3)
                elif atributo < atributo2:
                    print()
                    print(">>>>>>> " + segundo_jogador + " VOCÊ GANHOU!")
                    if segundo_jogador == jogador1:
                        pontos_player1 = pontos_player1 + pontos
                    elif segundo_jogador == jogador2:
                        pontos_player2 = pontos_player2 + pontos
                elif atributo == atributo2:
                    print()
                    print(">>>>>>> EMPATE!! NINGUÈM GANHA PONTOS!")
            contador += 1
        if pontos_player1 > pontos_player2:
            print()
            print(jogador1 + ' VOCÊ GANHOU A PARTIDA!')
            print('Este é seu score: %d ' % pontos_player1)
        elif pontos_player1 < pontos_player2:
            print()
            print(jogador2 + ' VOCÊ GANHOU A PARTIDA!')
            print('Este é seu score: %d ' % pontos_player2)
        elif pontos_player1 == pontos_player2:
            print()
            print('>>>>> EMPATE!')
        if (pontos_player2 > pontos_player1 and pontos_player2 > recorde):
            recorde = pontos_player2
            print()
            print(jogador2 + ' PARABÉNS VOCÊ É O NOVO RECORDISTA!')
        elif (pontos_player1 > pontos_player2 and pontos_player1 > recorde):
            recorde = pontos_player1
            print()
            print(jogador1 + ' PARABÉNS VOCÊ É O NOVO RECORDISTA')
    elif op == '2':
        print()
        print("O jogo é formado por dois jogadores.")
        print("O jogador 1 é responsável por escolher o número de rodadas na partida.")
        print("A cada rodada, cada jogador receberá 3 cartas aleatorias com 3 diferentes atributos")
        print("O jogador que irá iniciar a partida deve escolher uma carta, e nessa carta um atributo")
        print("Cada atributo tem um peso associado que corresponderá a pontuação que o vencedor da rodada receberá")
        print("O jogador 2 será capaz de ver a carta e o atributo escolhidos pelo jogador 1 ")
        print("O jogador 2 deverá escolher a carta que decidir mais adequada para combater o atributo já premeditado")
        print("Ao final de todas rodadas, vence o jogador que estiver com mais pontos.")
        print()
    elif op == '3':
        print("Fim de jogo! ")
    else:
        print("Opção inválida. Tente novamente")

