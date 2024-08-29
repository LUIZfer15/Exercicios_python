# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# Salário Bruto: (5 * 220)        : R$ 1100,00
# (-) IR (5%)                     : R$   55,00  
# (-) INSS ( 10%)                 : R$  110,00
# FGTS (11%)                      : R$  121,00
# Total de descontos              : R$  165,00
# Salário Liquido                 : R$  935,00

# Digite o salário
valor = float(input("Digite um valor ganho por hora: "))
horas = int(input("Digite quantas horas trabalhadas: "))

# Condição
bruto = valor*horas
ir1 = bruto*5/100
ir2 = bruto*10/100
ir3 = bruto*20/100
inss = bruto*10/100
fgts = bruto*11/100
liquido0 = bruto

# Desconto 1
desconto1 = ir1+inss
liquido1 = bruto-desconto1

# Desconto 2
desconto2 = ir2+inss
liquido2 = bruto-desconto2

# Desconto 3
desconto3 = ir3+inss
liquido3 = bruto-desconto3

# Imprimir o resultado
if bruto <= 900:
    print("O salário bruto é de R$ {}, isento de descontos e o salário liquído é de R$ {}".format(bruto,liquido0))
elif bruto >= 900 and bruto <= 1500:
    print("O salário bruto é de R$ {}, com os descontos de R$ {} o salário liquído é de R$ {}".format(bruto,desconto1,liquido1))
elif bruto >= 1500 and bruto <= 2500:
    print("O salário bruto é de R$ {}, com os descontos de R$ {} o salário liquído é de R$ {}".format(bruto,desconto2,liquido2))
elif bruto >= 2500:
    print("O salário bruto é de R$ {}, com os descontos de R$ {} o salário liquído é de R$ {}".format(bruto,desconto3,liquido3))