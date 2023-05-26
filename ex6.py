n1 = int(input("Digite o X: "))
n2 = int(input("Digite o Y: "))

soma = 0
for x in range(n1, n2):
    if x % 2 != 0:
        soma = soma + x
print("Somatória dos ímpares no intervalo: %d " %(soma))