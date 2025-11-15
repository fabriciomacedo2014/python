total_numPrimos = 0
num_user = int(input('DIgite um número: '))
for c  in range(1,num_user+1):
    if num_user % c == 0:
        total_numPrimos +=1
        print('\033[32m',end='')
    else:
        print('\033[31m', end='')
    print(c,end=' ')
print(f'\nVocê digitou o número {num_user}, ele é divisível {total_numPrimos} vezes')
if total_numPrimos == 2:
    print('É primo')
else:
    print('Não é primo')