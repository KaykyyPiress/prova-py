lista = [3, 5, 2, 9, 4, 8, 3, 7]
resto = []
original = []

for x in lista:
    if x % 2 == 0 or x % 3 == 0:
        original.append(x)
    else:
        resto.append(x)
        

print(*original, sep=' ')
print(*resto, sep=' ')

