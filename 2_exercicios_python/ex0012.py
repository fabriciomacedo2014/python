print('Desconto')
preco = float(input('Digite um preço: R$'))
desconto = preco - preco * (5/100)
print(f'O preço era de R${preco} e com o desconto de 5% temos R${desconto:.2f}')