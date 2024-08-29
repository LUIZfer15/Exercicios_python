# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

# Informe a sua altura
altura = float(input("Informe a sua altura: "))

# Calculo do peso ideal
peso = (72.7*altura)-58

# Imprimir o resultado
print("O peso ideal para a sua altura é {:.0f}kg".format(peso))