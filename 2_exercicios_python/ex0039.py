from datetime import datetime
ano_atual = datetime.today().year
nascimento_ano_cidadao = int(input('Digite sua data de nascimento: '))
idade = ano_atual - nascimento_ano_cidadao
#Caso a idade do cidadão seja menor de 18 anos
if idade < 18:
    diferenca = 18 - idade
    print(f'Quem nasceu em {nascimento_ano_cidadao} tem {idade}.')
    print(f'Ainda faltam {diferenca} anos para se alistar')
    print(f'Você vai se alistar em {ano_atual+diferenca}')
elif idade > 18:
    diferenca = idade - 18
    print(f'Quem nasceu em {nascimento_ano_cidadao} tem {idade} anos.')
    print(f'Seu alistamento foi há {diferenca} anos.')
    print(f'Seu alistamento foi em {ano_atual - diferenca}')
elif idade == 18:
    print(f'Quem nasceu em {nascimento_ano_cidadao} tem {idade} anos.')
    print(f'Seu alistamento deve ser feito IMEDIATAMENTE')