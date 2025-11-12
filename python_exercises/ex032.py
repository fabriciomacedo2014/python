from datetime import datetime
ano_atual = datetime.now().year
ano = int(input('Quer analisar qual ano? [0] para o ano atual: '))
if ano == 0:
    ano = ano_atual
if (ano % 4 == 0 and 100 != 0) or (ano % 100 == 0):
    print(f'O ano de {ano} é BISSEXTO..')
else:
    print(f'O ano de {ano} não é BISSEXTO..')