from math import hypot
cateto1 = float(input('Informe o cateto adjacente: '))
cateto2 = float(input('Informe o cateto oposto: '))
#usando modulos
hipotenusa_modulos = hypot(cateto1, cateto2)
print(hipotenusa_modulos)