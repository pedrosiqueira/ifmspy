def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


ocorrencias = letter_frequency(input("escreva uma frase:"))
for chave, valor in ocorrencias.items():
    print(f"{chave} ocorreu {valor} vez{'es' if valor>1 else ''}")
