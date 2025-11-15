from datetime import datetime
ano_atual = datetime.today().year
ano_Nascimento = int(input('Digite sua data de nascimento: '))
idade_Atleta = ano_atual - ano_Nascimento
print(f'O atleta tem {idade_Atleta} anos')
if idade_Atleta <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade_Atleta <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade_Atleta <= 19:
    print('CLASSIFICAÇÃO:  JUNIOR')
elif idade_Atleta <= 25:
    print('CLASSIFICAÇÃO:  SÊNIOR')
else:
    print('MASTER')