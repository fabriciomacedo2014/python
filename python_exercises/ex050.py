pares, soma = 0,0 #soma(armazena a soma total dos pares) e pares(armazena a quantidade de números pares)
for nums in range(1,7): #repete 6 vezes
    numeros = int(input(f'Digite o {nums}º número: ')) #números do usuário
    if numeros % 2 == 0: # verifica se é par
        pares +=1 # incrementa a quantidade de pares
        soma += numeros # soma os números pareces recebidos
#exibição dos queridos dados
print(f'Temos no total {pares} números PARES')
print(f'Somando esses números PARES, temos {soma} como soma total.')