from random import randint
print ('''Seja bem vindo ao jogo PEDRA, PAPEL, TESOURA, LAGARTO, SPOCK 
O Campeão é o que atingir três pontos primeiro. 
Lembrando que: Tesoura corta papel;Papel cobre pedra;Pedra esmaga lagarto;Lagarto envenena Spock;Spock esmaga tesoura;Tesoura decapita lagarto;Lagarto come papel;Papel refuta Spock;Spock vaporiza pedra; Pedra quebra tesoura
Vamos Jogar!''' )
rodada =  (0)
Pontos_player1 = int (0)
Pontos_computer = int(0)
papel = int (1)
pedra = int (2)
tesoura = int (3)
lagarto = int (4)
spock =  int (5)
while (Pontos_player1 < 3) or (Pontos_computer < 3):
    if Pontos_computer == 3:
        print('O jogo acabou!Você Perdeu...')
        break
    if Pontos_player1 == 3:
         print('Parabens você ganhou!! Você é monstro')
         break
    computer = randint(1,5)
    print ("Coputador está pronto! Faça sua escolha!")
    player1 = int (input ("Escolha:  1 para papel, 2 para pedra, 3 para tesoura, 4 para lagarto ou 5 para spock"))
    if computer == player1:
      print ("It's a draw, try again")
    else:
      lista = [computer, player1]
      lista_derrota = [ [3,1], [1,2], [2,4], [4,5], [5,3], [3,4], [4,1], [1,5], [5,2], [2,3] ]
      if lista in lista_derrota:
            Pontos_computer = Pontos_computer +1
            Pontos_player1 = 0
            print ("Computer Wins!")
      else :
           Pontos_player1 = Pontos_player1 +1
           Pontos_computer = 0
           print ("YOU WIN!")
    rodada = rodada + 1
    print(Pontos_computer)
    print(Pontos_player1)
    
