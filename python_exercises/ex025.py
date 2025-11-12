nome_completo_user = str(input('Digite seu nome: ')).lower()
if 'macedo' in nome_completo_user:
    print('Seu nome contém "Macedo"')
else:
    print('Seu nome não contém "Macedo"')
#sem condição
nome_completo = str(input('Digite seu nome: ')).lower()
contem = 'macedo' in nome_completo
print(contem)