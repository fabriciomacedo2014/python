n1 = int(input('I need a number, please: '))
n2 = int(input('Perfect, but I need other number: '))
plus = n1 + n2
multi = n1 * n2
subtraction = n1 - n2
int_div = n1 % n2
powTencia = n1 ** n2
modlue = n1 // n2
division = n1 / n2
print(f"""Temos aqui:
soma = {plus}
subtracao = {subtraction}
multiplicacao = {multi}
divisão inteira = {int_div}
potencia = {powTencia}
modulo = {modlue}
divisão = {division:.2f}
""")