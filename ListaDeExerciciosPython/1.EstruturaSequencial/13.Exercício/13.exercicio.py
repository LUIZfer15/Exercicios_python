# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# Informe a sua altura
altura = float(input("Informe a sua altura: "))

# Calculo do peso ideal
h = (72.7*altura)-58
m = (62.1*altura) - 44.7

# Imprimir o resultado
print("O peso ideal para a sua altura é {:.0f}kg(Homem) e {:.0f}Kg(Mulher)".format(h,m))