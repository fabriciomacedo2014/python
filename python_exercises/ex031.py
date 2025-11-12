distancia_viagem = int(input('Qual a distância da viagem? '))
viagens_curtas = 0.50
viagens_longas = 0.45
if distancia_viagem < 200:
    preco_passagemCurta = distancia_viagem * viagens_curtas
    print(f'O preço da passagem é de R${preco_passagemCurta:.2f}')
else:
    preco_passagemLonga = distancia_viagem * viagens_longas
    print(f'O preço da passagem é de R${preco_passagemLonga:.2f}')
