nome_pessoa = str(input('Digite seu nome: '))
primeiro_nome = nome_pessoa.split()
sem_espace = nome_pessoa.replace(' ','')

print(f'Seu nome em maiúsculas é {nome_pessoa.upper()}')
print(f'Seu nome em minúsculas é {nome_pessoa.lower()}')
print(f'Seu nome ao todo tem {len(sem_espace)} letras')
print(f'Seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras')