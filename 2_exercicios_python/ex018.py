import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo de SENO é {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O COSSENO é {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'Para finalizar temos a TANGENTE que é {tangente:.2f}')