# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# Digite a área do quadrado
lado = float(input("Digite o lado do quadrado: "))

# Calcular a área do quadrado
area = lado*lado

# Calcular o dobro da área
dobro = area+area

# Imprimir o resultado
print("A área do quadrado é {} e o dobro é igual a {}".format(area,dobro))