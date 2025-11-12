cidade_nasc_user = str(input('Em que cidade você nasceu? ')).lower()
if 'novo' in cidade_nasc_user:
    print('Sua cidade contém "NOVO"')
else:
    print('Sua cidade não contém "NOVO"')
#Sem condição
cidade_nasc = str(input('Em que cidade você nasceu? ')).lower()
novo =  'novo' in cidade_nasc
print(novo)