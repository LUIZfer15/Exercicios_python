# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

# Informe 3 produtos
p1 = float(input("Informe o preço do primeiro produto: "))
p2 = float(input("Informe o preço do segundo produto: "))
p3 = float(input("Informe o preço do terceiro produto: "))

# Variável
valor_min = min(p1,p2,p3)

# Imprimir o resultado
print("O produto mais barato está com valor de {:.2f}".format(valor_min))