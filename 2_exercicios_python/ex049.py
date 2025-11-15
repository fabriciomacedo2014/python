opcoes = [1,2,3,4]
print('Tabuada')
print('''Painel
[1] Soma
[2] Subtração
[3] Divisão
[4]  Multiplicação''')
try:
    escolha_user = int(input('Digite uma opção: '))
    if escolha_user not in opcoes:
        print('Digite um número dentro das opções.')
    elif escolha_user == 1:
        num = int(input('Digite um número para ver sua tabuada de SOMA: '))
        for c in range(1,11):
            print(f'{num} + {c} = {num + c}')
    elif escolha_user == 2:
        num = int(input('Digite um número para ver sua tabuada de SUBTRAÇÃO: '))
        for c in range(1, 11):
            print(f'{num} - {c} = {num - c}')
    elif escolha_user == 3:
        num = int(input('Digite um número para ver sua tabuada de DIVISÃO: '))
        for c in range(1, 11):
            print(f'{num} / {c} = {num / c:.2f}')
    elif escolha_user == 4:
        num = int(input('Digite um número para ver sua tabuada de MULTIPLICAÇÃO: '))
        for c in range(1, 11):
            print(f'{num} x {c} = {num * c}')
except ValueError:
    print('Digite um valor válido')