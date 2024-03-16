file = open(input("caminho do arquivo: "))

i = 1
for line in file:
    print(i, line, end="")
    i += 1

file.close()
