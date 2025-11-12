print('CONVERSOR DE METROS PARA CM E MM')
print("""PAINEL DE OPÇÕES
[1] Centimentos(cm)
[2] Milimetros(mm)""")
option = int(input('Escolha alguma das opções: '))
if option == 1:
    m_to_cm = float(input('Quantos metros deseja converter para centímetros? '))
    cm = m_to_cm * 100
    print(f'{m_to_cm} metros convertido para centímetros é {cm}cm')
else:
    m_to_mm = float(input('Quantos metros deseja converter para milímetros?'))
    mm = m_to_mm * 1000
    print(f'{m_to_mm} metros convertido para milímetros é {mm}mm')