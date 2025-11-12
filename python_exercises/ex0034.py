salario_atual = float(input('Qual seu salário? '))
if salario_atual >= 1250:
    aumento15 = salario_atual + salario_atual * (10/100)
    print(f'Seu salário com 10% de aumento: R${aumento15:.2f}')
elif salario_atual < 1250:
    aumento10 = salario_atual + salario_atual * (15/100)
    print(f'Seu salário com 10% de aumento: R${aumento10}')
