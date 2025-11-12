n1 = int(input('One number, please: '))
n2 = int(input('Other number, please: '))
sum = n1 + n2
product = n1 *  n2
if product <= 1000:
    print(f'O produto é menor que 1000, portanto temos sua multiplicação {product}')
else:
    print(f'O produto é maior que 1000, portanto temos sua soma {sum}')

