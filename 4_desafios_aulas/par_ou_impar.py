num = int(input('Digite um número; (0 para parar)'))
while num != 0:
    if num % 2 == 0:
        print('Par')
        num = int(input('Digite um número; (0 para parar)'))
    elif num % 2 != 0:
        print('impar')
        num = int(input('Digite um número; (0 para parar)'))
print('Finalizado!')
