print('IMC')
peso = float(input('Qual é seu peso? Kg'))
altura = float(input('Qual sua altura? '))
formula_IMC = peso / (altura * altura)
if formula_IMC < 18.5:
    print(f'Seu IMC é {formula_IMC:.1f} Você está em Abaixo do peso.')
elif formula_IMC < 25:
    print(f'Seu IMC é {formula_IMC:.1f} Você está em Peso normal')
elif formula_IMC < 30:
    print(f'Seu IMC é {formula_IMC:.1f} Você está em Sobrepeso')
else:
    print(f'Seu IMC é {formula_IMC:.1f} Você está em Obesidade.')