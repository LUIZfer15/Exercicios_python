# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. O produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

# Digite um número inteiro
n1 = int(input("Digite um número inteiro: "))

# Digite outro número inteiro
n2 = int(input("Digite outro número inteiro: "))

# Digite um número real
r = float(input("Digite um número real: "))

# a.
a = (n1+n1)+(n2/2)

# b.
b = (n1+n1+n1)+r

# c.
c = r*r

# Imprimir o resultado
print("O resultado da questões a.{}, b.{} e c.{}".format(a,b,c))