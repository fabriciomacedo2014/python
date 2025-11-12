import random
velCidade = float(input('Qual a velocidade do veículo? '))
fator_Velocidade = random.randint(3,11)
velocidade_limite = fator_Velocidade * 10
if velCidade > velocidade_limite:
    multa = (velCidade - velocidade_limite) * 7
    print(f'Você ultrapassou o límite de {velocidade_limite}km/h, sua multa é de R${multa:.1f} reais.')
else:
    print(f'O limite da velocidade da Avenida Macedo é {velocidade_limite}km/h.')
    print('Prossiga.')
print('Dirija com cuidado.')