try:
    valor_inicial = int(input('Digite o valor inicial: '))
    valor_final = int(input('Digite o fim: '))
    passo = int(input('Digite o passo (pulando de): '))
    for c in range(valor_inicial, valor_final, passo):
            print(c, end=' ')
except ValueError:
    print('Digite um valor válido.')

print('FIM')
