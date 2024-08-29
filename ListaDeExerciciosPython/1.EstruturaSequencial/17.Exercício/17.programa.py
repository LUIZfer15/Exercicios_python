# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# Digite quantos metros quadrados devem ser pintados
area = float(input("Qual o tamanho em metros quadrados da area a ser pintada? "))

# Variáveis
litros = area/6
latas = litros/18

# Condição
if  latas % 18 != 0:
    latas += 1
custo = latas*80

galoes = litros/3.6
if galoes % 3.6!=0:
    galoes += 1
custo2 = galoes*25

# Mistura de latas e galoes
mistura_lata = int(litros/18.0)
mistura_galao = int((litros - (mistura_lata*18))/3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

# Imprimir o resultado
print("Apenas latas de 18 litros: {:.1f}L preço: R$ {:.2f}".format(latas,custo))
print("Apenas galões de 3,6 litros: {:.1f}L preço: R$ {:.2f}".format(galoes,custo2))
print ("Mistura: {} latas e {} galoes = {:.2f}".format(mistura_lata, mistura_galao, ( mistura_lata  *  80 ) + ( mistura_galao  *  25 )))