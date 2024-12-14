# Lista proibida. Ler um número n, seguido por n palavras "proibidas". Depois, ler um número m, seguido por m frases, uma em cada linha. Para cada frase, escrever "CENSURADO" ou "PERMITIDO" caso haja palavras proibidas ou não.

proibidas = set()

n = int(input("quantas palavras proibidas?"))
print("digite uma palavra proibida em cada linha")
for _ in range(n):
    proibidas.add(input())

m = int(input("quantas frases a filtrar?"))
print("digite uma frase em cada linha")
for _ in range(m):
    frase = input()
    permitida = True
    for palavra in frase.split():
        if palavra in proibidas:
            permitida = False
            break
    print("PERMITIDO" if permitida else "CENSURADO")
