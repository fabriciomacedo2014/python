frase = str(input('Digite uma frase: ')).upper()
achar = str(input('O que você deseja encontrar na frase? ')).upper()
procurador = frase.find(achar)
if procurador != -1:
    print(f'Encontrado na posição {procurador}')
else:
    print('Não encontrado')