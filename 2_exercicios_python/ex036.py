valor_casa = float(input('Qual o valor da casa? R$'))
salario_comprador = float(input('Quanto recebe o comprador? R$'))
anos_pagamentos = int(input('Planeja pagar em quantos anos? '))
minimo = salario_comprador * (30 / 100)
prestacao = valor_casa / (anos_pagamentos * 12)
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos_pagamentos} anos' ,end=' ')
print(f'a prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo negado')