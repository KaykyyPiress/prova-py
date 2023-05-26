digite = int(input("Digite a ordem da matriz: "))

m = []

for num_linha in range(digite):
    linha = []
    for num_coluna in range(digite): 
        linha.append(2**(num_linha + num_coluna))
    m.append(linha)

for linha in range(len(m)):
    for coluna in range (len(m[linha])):
        print("%4d" % m[linha][coluna], end="")
    print ()

"""""""""
n = int(input("Digite a ordem da matriz: "))

matriz = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        matriz[i][j] = 2**(i+j)

for linha in matriz:
    for item in linha:
        print("{:4d}".format(item), end="")
    print()
"""