from random import randint
itens = ['PEDRA', 'PAPEL', 'TESOURA']
print('Pedra, papel e tesoura.')
print('''PAINEL:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
try:
    maquina = randint(0,2)
    jogador = int(input('Escolha: '))
    if jogador not in [0,1,2]:
        print('TENTE NOVAMENTE')
    else:
        print(f'JOGADOR jogou {itens[jogador]}')
        print(f'MÁQUINA jogou {itens[maquina]}')
        if jogador == maquina:
            print('EMPATE')
            #ABAIXO É ONDE O JOGADOR VENCE
        elif (jogador == 0 and maquina == 2) or \
                (jogador == 1 and maquina == 0) or \
                (jogador == 2 and maquina == 1):
            print('JOGADOR VENCE')
            #ABAIXO É O QUE ACONTECE QUANDO A 3º CONDIÇÃO É FALSA
        else:
            print('MÁQUINA VENCE')
except ValueError:
    print('Entrada inválida.')
