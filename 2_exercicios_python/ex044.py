
print('Empório dos Tecidos')
valorTot = float(input('PREÇOS TOTAL DAS COMPRAS: '))
print('''PAINEL:
[1] á vista 
[2] á vista no cartão
[3] 2x no cartão
[4] 3x no cartão''')
opcao = int(input('Digite a opção escolhida: '))
if opcao == 1:#pagar a vista com 10% de desconto
    desconto1 = valorTot - (valorTot * 10/100)
    print(f'Sua compra era de R${valorTot:.2f} reais.')
    print(f'O total das suas compras vai ser R${desconto1:.2f}')
elif opcao == 2:#a vista no cartão com 5% de desconto
    desconto2 = valorTot - (valorTot * 5/100)
    print(f'O total das suas compras vai ser R${desconto2:.2f}')
elif opcao == 3:#pagar 2x no cartão sem juros
    parcelas = valorTot / 2
    print(f'Você vai pagar duas parcelas de R${parcelas:.2f} reais.')
elif opcao == 4:#pagar 3x no cartão com 20% de juros
    juros20 = valorTot + (valorTot * 20/100)
    parcelas3x = juros20 / 3
    print(f'Você vai pagar três parcelas de R${parcelas3x:.2f} reais.')
    print(f'Sua compra vai dar R${juros20:.1f} reais')
