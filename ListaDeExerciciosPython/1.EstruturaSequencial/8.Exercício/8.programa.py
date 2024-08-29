# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# Informe quanto você ganha por hora
qtn = float(input("Quanto você ganha por hora? "))

# Informe o número de horas trabalhadas
hora = int(input("Quantas horas trabalhadas? "))

# Informe o número de dias no mês
mes = int(input("Quantos dias do mês? "))

# Calcule o total do salário no final do mês
salario = mes*qtn*hora

# Imprimir o resultado
print("O seu salário mensal é {}".format(salario))