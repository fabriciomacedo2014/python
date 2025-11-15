soma = 0
val_totais = 0
for n in range(1,501,2):
    if n % 3 == 0:
        soma = soma+ n
        val_totais += 1
print(f'Temos no total {val_totais} valores')
print(f'A soma de todos os valores solicitados é {soma}')