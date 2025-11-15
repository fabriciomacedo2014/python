print("Médias das 3 notas")
aluno = str(input('Digite o nome do aluno: '))
print('Vamos agora para as notas')
nota1 = float(input('Qual a primeira nota do aluno? '))
nota2 = float(input('Qual a segunda nota do aluno? '))
nota3 = float(input('Qual a terceira nota do aluno? '))
media = (nota1 + nota2  + nota3) / 3
print('='*20)
print(f'Aluno(a) {aluno.upper()} teve sua média final {media:.2f}')
print("""Deseja saber se ele estar de recuperação? \n
[1] sim
[2] não""")
options = int(input('Digite alguma das opções: '))
if options == 1:
    print('Certo, vamos calcular.')
    if media > 6:
        print('aprovado')
    else:
        print('reprovado')