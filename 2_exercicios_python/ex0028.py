import random
cont = 1
num_PC = random.randint(0,10)
user_choice = int(input('Digite um número de 0 a 10; '))
while user_choice != num_PC:
    cont +=1
    print('Tente novamente')
    user_choice = int(input('Digite um número de 0 a 10; '))
print(f'Você acertou e tentou {cont} vezes')