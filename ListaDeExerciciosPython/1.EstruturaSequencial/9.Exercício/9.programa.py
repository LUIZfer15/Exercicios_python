# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius / C = 5 * ((F-32) / 9).

# Digite o valor de uma temperatura
f = int(input("Digite a temperatura em graus Fahrenheit: "))

# Calculo de Fahrenheit para Celsius
c = 5 * ((f-32) / 9)

# Imprimir o resultado
print("A temperatura de {}°F equivale a {:.0f}°C".format(f,c))