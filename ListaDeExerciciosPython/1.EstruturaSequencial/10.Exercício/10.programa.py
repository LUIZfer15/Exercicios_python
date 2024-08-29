# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# Digite o valor de uma temperatura
c = int(input("Digite a temperatura em graus Celsius: "))

# Calculo de Celsius para Fahrenheit
f = c*1.8+32

# Imprimir o resultado
print("A temperatura de {}°C equivale a {:.0f}°F".format(c,f))