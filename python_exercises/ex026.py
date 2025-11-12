frase_user = str(input('Digite uma frase: ')).lower()
letra = str(input('Que letra que você deseja encontrar? ')).lower()
a_quantDade = frase_user.count(letra)
a_apari = frase_user.find(letra)+1
a_ultiVez = frase_user.rfind(letra)+1
print(f'A letra {letra.upper()} apareceu {a_quantDade} vezes na frase.')
print(f'A primeira aparição da {letra.upper()} foi na posição {a_apari}.')
print(f'A últma vez que a letra {letra.upper()} apareceu foi na posição {a_ultiVez}.')