# exclui o conteúdo da pasta do usuário e da pasta temporária
Remove-Item -Path "C:\Users\aluno\*" -Recurse -Force
# exclui o conteúdo da pasta temporária
# Remove-Item -Path "$env:TEMP\*" -Recurse -Force

$username = "aluno"
$password = ConvertTo-SecureString "alunoifms" -AsPlainText -Force

# executa um comando com outra credencial solicitada
# Start-Process powershell -Credential (Get-Credential) -ArgumentList "SeuComando"

# executa um script com outra credencial solicitada
# Start-Process -FilePath "powershell" -ArgumentList "-File 'C:\Caminho\Para\SeuScript.ps1'" -Credential (Get-Credential) -NoNewWindow

# executa um comando com a credencial configurada
# $credential = New-Object System.Management.Automation.PSCredential($username, $password)
# Start-Process powershell -Credential $credential -ArgumentList "SeuComando"

# permissão de execução de scripts
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# executa o script
& "\\10.8.32.3\arquivos\Arquivos curso superior\tads-algoritmos\02-instalando-ambiente-python.ps1"

# executa os scripts com a credencial configurada
$credential = New-Object System.Management.Automation.PSCredential($username, $password)
Start-Process -FilePath "powershell" -ArgumentList "-File '\\10.8.32.3\arquivos\Arquivos curso superior\tads-algoritmos\03-preparando-ambiente-python.ps1'" -Credential $credential -NoNewWindow
Start-Process -FilePath "powershell" -ArgumentList "-File '\\10.8.32.3\arquivos\Arquivos curso superior\tads-algoritmos\04-baixando-prova.ps1'" -Credential $credential -NoNewWindow
