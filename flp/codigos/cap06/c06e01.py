# Ler uma sequência de números, que se encerra com um número repetido. Escrever os números ordenadamente.

numeros = set()
numero = int(input())
while numero not in numeros:
    numeros.add(numero)
    numero = int(input())
print(sorted(list(numeros)))
# a linha acima é equivalente à essas três linhas abaixo:
# mylist = list(numeros)
# sortedlist = sorted(mylist)
# print(sortedlist)
