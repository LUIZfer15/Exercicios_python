# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# Informe o tamanho do arquivo e a velocidade de internet
mb = float(input("Informe o tamanho do arquivo em MB: "))
internet = float(input("Informe a velocidade do link em Mbps: "))

# Variáveis
tempo = mb/internet
min = tempo/60

# Imprimir resultado
print("O tempo aproximado de download do arquivo em minutos será de {:.1f} minutos".format(min))