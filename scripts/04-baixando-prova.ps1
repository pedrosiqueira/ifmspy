# Caminho do arquivo zip e local de destino
$zipFilePath = "\\10.8.32.3\arquivos\Arquivos curso superior\tads-algoritmos\prova.zip"
$destinationPath = "C:\Users\aluno\Desktop"

# Descompacta o arquivo zip no local de destino
Expand-Archive -Path "$zipFilePath" -DestinationPath "$destinationPath"
