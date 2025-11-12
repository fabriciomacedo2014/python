valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
maior_valor = max(valor1,valor2,valor3)
menor_valor = min(valor1,valor2,valor3)
if valor1 == valor2 == valor3:
    print('Todos os números são iguais')
else:
    print(f'O maior número é {maior_valor}')
    print(f'O menor número é {menor_valor}')