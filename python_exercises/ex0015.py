dias_alugados = int(input('Quantos dias alugados? '))
kms_rodados = int(input('Quantos Km rodados? '))
dias_alugados_custo = 60  # custos dos dias
km_rodados_custo = 0.15  # custo dos kms rodados

alugados_dia_total = dias_alugados_custo * dias_alugados  #total, geral dos dias
km_tota = kms_rodados * km_rodados_custo #total, geral dos km custo

geral = km_tota + alugados_dia_total
print(f"O gasto total foi de R${geral:.2f}")
