# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

# Informe quanto você ganha por hora
qtn = float(input("Quanto você ganha por hora? "))

# Informe o número de horas trabalhadas
hora = int(input("Quantas horas trabalhadas? "))

# Informe o número de dias no mês
mes = int(input("Quantos dias do mês? "))

# Variáveis
bruto = qtn*hora*mes

imposto_renda = bruto*11/100

inss = bruto*8/100

sindicato = bruto*5/100

liquido = bruto-imposto_renda-inss-sindicato

# Salário bruto
print("Salário bruto é de R$ {:.2f}".format(bruto))

# Imposto de Renda
print("O valor pago de Imposto de Renda é de R$ {:.2f}".format(imposto_renda))

# INSS
print("O valor pago para o INSS é de R$ {:.2f}".format(inss))

# Sindicato
print("O valor pago para o Sindicato é de R$ {:.2f}".format(sindicato))

# Salário líquido
print("Salário líquido é de R$ {:.2f}".format(liquido))