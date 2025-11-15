from math import trunc
import random
print('Parte inteira de um número')
print('''
Painel
[1] Desejo digitar o número
[2] Áleatorio ''')
options = int(input('Escolha uma opção: '))
while options != 1 and options != 2:
    options = int(input('Escolha uma opção: '))
if options == 1:
    num_usuario = float(input('Digite o número: '))
    parte_InteiraInt = trunc(num_usuario)
    print(f'O número escolhido foi {num_usuario} e sua parte inteira é {parte_InteiraInt}')
elif options == 2:
    aleatorio = random.uniform(1,100)
    inteiro = trunc(aleatorio)
    print(f'O número áleatorio escolhido foi {aleatorio:.3f} e sua parte inteira é {inteiro}')