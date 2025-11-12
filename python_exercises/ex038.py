primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
if primeiro_valor > segundo_valor:
    print('O primeiro valor é o maior')
elif segundo_valor > primeiro_valor:
    print('O segundo valor é o maior')
else:
    print("Ambos valores são iguais")