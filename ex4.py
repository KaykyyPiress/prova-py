def inverte_string(texto):
    # Inverte a string
    texto_invertido = texto[::-1]
    # Converte todas as letras em minúsculas
    texto_invertido_minusculo = texto_invertido.lower()
    return texto_invertido_minusculo

text = input("Digite o texto: ")

print(inverte_string(text))