# Faça um Programa que converta metros para centímetros e mílimetros.

# Digitar uma distância em metros
medida = float(input("Uma distância em metros: "))

# Calcular as medidas
cm = medida * 100
mm = medida * 1000

# Imprimir o resultado
print("A medida de {:.0f}m corresponde a {:.0f}cm e {:.0f}mm".format(medida, cm, mm))