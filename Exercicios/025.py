'''
Crie um programa para jogar JOKEMPO, usando a função random.randint
'''

import random
#ESTE IMPORT TIME É UTILIZADO APENAS PARA ESTILIZAR, NÃO É NECESSARÁRIO
import time
pontos_pc = 0
pontos_jogador = 0
contador = 0
#EU UTILIZEI O WHILE APENAS PARA TESTE, NÃO ERA O OBJETIVO DO PROJETO
while contador < 3:
    contador += 1
    pc = random.randint(1, 3)
    jogada = int(input('Digite uma jogada, 1-Pedra, 2-Papel, 3-Tesoura: '))
    if jogada < 1 or jogada > 3:
        print('Digite um valor entre 1 e 3')

    else:
        '''PARA SITUAÇÕES DE EMPATE EU PODERIA FAZER APENAS: 
                *IF PC == JOGADA*
                    *PRINT('EMPATE')*
        '''

        '''EU PODERIA TAMBÉM SEPARAR OS GANHOS DAS PERDAS, FAZENDO:
                *IF J = PC*
                    PRINT('EMPATE')
                ELIF ((J == 3 AND PC == 2)) OR
                (J == 2 AND PC == 1) OR
                (J == 1 AND PC == 3):
                PRINT('VOCÊ GANHOU')
            ELSE:
                PRINT('VOCÊ PERDEU') 
        '''
        print('----------------//-----------------')
        time.sleep(1)
        print('JO')
        time.sleep(1)
        print('KEM')
        time.sleep(1)
        print('PÔ!')
        time.sleep(0.5)
        print('----------------//-----------------')
        print(f'O Computador joga: {pc} e o jogador joga: {jogada}')
    if pc == 1 and jogada == 1:
        print('O resultado é empate')
    elif pc == 1 and jogada == 2:
        print('O Computador ganhou')
        pontos_pc += 1
    elif pc == 1 and jogada == 3:
        print('O Jogador ganhou')
        pontos_jogador += 1
    elif pc == 2 and jogada == 1:
        print('O Computador ganhou')
        pontos_pc += 1
    elif pc == 2 and jogada == 2:
        print('o resultado é empate')
    elif pc == 2 and jogada == 3:
        print('O Jogador ganhou')
        pontos_jogador += 1
    elif pc == 3 and jogada == 1:
        print('O Jogador ganhou')
        pontos_jogador += 1
    elif pc == 3 and jogada == 2:
        print('O Computador ganhou')
        pontos_pc += 1
    elif pc == 3 and jogada == 3:
        print('O resultado é empate')

print(f'No fim de 3 jogos o Computador fez: {pontos_pc} ponto(s) e o Jogador fez {pontos_jogador} ponto(s)')

#Utilizei o While só pra testar
