import random
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
alunos_total = random.choice([aluno1,aluno2,aluno3,aluno4])
print(f'O aluno escolhido foi {alunos_total}')
