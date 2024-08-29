# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

# Digite o salário
valor = float(input("Digite um salário: "))

# Variável
a = valor*20/100+valor
b = valor*15/100+valor
c = valor*10/100+valor
d = valor*5/100+valor

# Repetição
while (valor <= 0):
    valor = float(input("Digite um salário válido: "))
    
# Imprimir o resultado
if valor <= 280:
    print("O salário de R$ {:.2f} teve um aumento de 20%, e o novo salário ficou igual a R$ {:.2f}. ".format(valor,a))
elif valor >= 280 and valor <= 700:
    print("O salário de R$ {:.2f} teve um aumento de 15%, e o novo salário ficou igual a R$ {:.2f}. ".format(valor,b))
elif valor >= 700 and valor <= 1500:
    print("O salário de R$ {:.2f} teve um aumento de 10%, e o novo salário ficou igual a R$ {:.2f}. ".format(valor,c))
elif valor >= 1500:
    print("O salário de R$ {:.2f} teve um aumento de 5%, e o novo salário ficou igual a R$ {:.2f}. ".format(valor,d))