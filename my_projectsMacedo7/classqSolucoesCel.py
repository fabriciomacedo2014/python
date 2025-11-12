print('CLASSIFICADOR DE SOLUÇÕES CELULARES')
dentro = float(input('Digite a concentração DENTRO da célula (em mol): '))
fora = float(input('Digite a concentração FORA da célula (em mol): '))
if dentro == fora:
    print('A solução é ISOTÔNICA')
    print('A célula está em um equilíbrio osmótico.')
elif fora > dentro:
    print('A solução é HIPERTÔNICA.')
    print('A água sai da célula, assim ela pode murchar(plasmólise)')
else:
    print('A solução é HIPOTÔNICA.')
    print('A célula tem grande quantidade de água, \n '
          'assim ela pode inchar ou se romper(lise)')
