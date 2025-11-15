import random
jogador = int(input('Digite um número: '))
maquina = random.randint(0,10)
soma = jogador + maquina
#escolha de par ou impar
escolha = input('Par ou Impar? [P] ou [I]').strip().upper()
resultado = soma % 2
#condições
if resultado == 0:
    print('PAR')
    vencedor = 'P'
else:
    print('IMPAR')
    vencedor = 'I'
if escolha[0] == vencedor:
    print('Você venceu!')
else:
    print('A máquina venceu!')
print(f'Jogador =  {jogador}')
print(f'Máquina = {maquina}')