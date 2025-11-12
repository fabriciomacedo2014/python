print('MÉDIA DE NOTAS')
nota1  = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média foi {media:.1f} STATUS: REPROVADO!!!!!')
elif media > 5.0 or media < 6.9:
    print('RECUPERAÇÃO!')
elif media >= 7:
    print('APROVADO')