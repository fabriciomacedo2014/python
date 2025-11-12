num_user = int(input('Digite um número: '))
unidade_milhar = num_user // 1000 % 10
centena = num_user // 100 % 10
dezena = num_user // 10 % 10
unidade = num_user % 10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Unidade de milhar: {unidade_milhar}')
