
temperatura = float(input('Digite a temperatura em C°: '))
celsius_to_fah = (temperatura * 1.8) + 32
print(f'{temperatura:.0f}Cº em Fahrenheit é {celsius_to_fah}')
fah_to_cel = (celsius_to_fah - 32) / 1.8
print(f"A temperatura em Fahrenheit é {celsius_to_fah}, mas em Celsius é {fah_to_cel:.2f}")