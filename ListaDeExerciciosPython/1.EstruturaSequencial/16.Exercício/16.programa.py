# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# Digite quantos metros quadrados devem ser pintados
area = float(input("Qual o tamanho em metros quadrados da area a ser pintada? "))

# Variáveis
tinta = area/3
latas = area/18

if  latas % 18 != 0:
    latas += 1
custo = latas*80

# Imprimir o resultado
print("Sua parede tem a área de {}m².".format(area))
print("Para pintar essa parede, você vai precisar de {}l de tinta.".format(tinta))
print("Para comprar você vai gastar R$ {:.2f}".format(custo))