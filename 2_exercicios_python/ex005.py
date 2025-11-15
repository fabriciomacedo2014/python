print("""[1] inteiros
[2] racionais""")
option = int(input('escolha alguma opção: '))
if option == 1:
    num_inteiro = int(input('Digite o seu número inteiro: '))
    num_sucessor_inteiro = num_inteiro + 1
    num_antecessor_inteiro = num_inteiro - 1
    print(f'Sucessor do número {num_inteiro} é {num_sucessor_inteiro}')
    print(f'Antecessor do número {num_inteiro} é {num_antecessor_inteiro}')
elif option == 2:
    aproxim_racionais = float(input('Digite o seu número racional: '))
    sucessor_racionais = aproxim_racionais + 1
    antecessor_racionais = aproxim_racionais - 1
    print(f'Sucessor do número {aproxim_racionais} é {sucessor_racionais:.2f}')
    print(f'Antecessor do número {aproxim_racionais} é {antecessor_racionais}')
