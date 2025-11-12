num = int(input('Digite um número para realizar sua conversão: '))
print('''PAINEL DE OPÇÕES:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
 ''')
painel = int(input('Digite a opção escolhida: '))
if painel == 1:
    binario = bin(num)[2:]
    print(f"{num} convertido para BINÁRIO é {binario}")
elif painel == 2:
    octal = oct(num)[2:]
    print(f"{num} convertido para OCTAL é {octal}")
else:
    hexadecimal = hex(num)[2:]
    print(f"{num} convertido para HEXADECIMAL é {hexadecimal}")