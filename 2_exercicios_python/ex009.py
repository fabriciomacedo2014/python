print('TABUADA')
print('''Painel:
 [1] soma
 [2] subtração
 [3] multiplicação
 [4] divisão''')
option = int(input('Digite uma opção: '))
if option == 1:
    num = int(input('Digite um número para ver sua tabuada: '))
    for cont in range(1, 11):
        print(f'{num} + {cont} = {num + cont}')
elif option == 2:
    num = int(input('Digite um número para ver sua tabuada: '))
    for cont in range(1, 11):
        print(f'{cont} - {num} = {cont - num}')
elif option == 3:
    num = int(input('Digite um número para ver sua tabuada: '))
    for cont in range(1,11):
        print(f'{cont} * {num} = {cont * num}')
elif option == 4:
    num = int(input('Digite um número para ver sua tabuada: '))
    for cont in range(1,11):
        print(f'{cont} / {num} = {cont / num:.2f}')