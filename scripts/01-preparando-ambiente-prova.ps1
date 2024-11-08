# exclui o conteúdo da pasta do usuário
Remove-Item -Path "C:\Users\aluno\*" -Recurse -Force

$script1 = "https://raw.githubusercontent.com/pedrosiqueira/ifmspy/refs/heads/main/scripts/02-instalando-ambiente-python.ps1"
$script2 = "https://raw.githubusercontent.com/pedrosiqueira/ifmspy/refs/heads/main/scripts/03-preparando-ambiente-python.ps1"
$script3 = "https://raw.githubusercontent.com/pedrosiqueira/ifmspy/refs/heads/main/scripts/04-baixando-prova.ps1"

# define a política de execução de script desta sessão atual de terminal para RemoteSigned (permissão de executar scripts) sem solicitar confirmação (-Force)
Set-ExecutionPolicy RemoteSigned -Scope Process -Force;

# executa o script online
(New-Object System.Net.WebClient).DownloadString($script1) | Invoke-Expression

# Define o código para abrir uma nova instância do PowerShell sem privilégios elevados
$code1 = "Set-ExecutionPolicy RemoteSigned -Scope Process -Force; (New-Object System.Net.WebClient).DownloadString('$script2') | Invoke-Expression"
$code2 = "Set-ExecutionPolicy RemoteSigned -Scope Process -Force; (New-Object System.Net.WebClient).DownloadString('$script3') | Invoke-Expression"

# Abre o PowerShell no contexto do usuário atual, sem privilégios administrativos, e executa o script
Start-Process -FilePath "powershell" -ArgumentList "-NoProfile", "-NoExit", "-Command", $code1 -Verb RunAsUser
Start-Process -FilePath "powershell" -ArgumentList "-NoProfile", "-NoExit", "-Command", $code2 -Verb RunAsUser

# exclui o conteúdo da pasta temporária
# Remove-Item -Path "$env:TEMP\*" -Recurse -Force

# $username = "aluno"
# $password = ConvertTo-SecureString "alunoifms" -AsPlainText -Force

# executa um comando com outra credencial solicitada
# Start-Process powershell -Credential (Get-Credential) -ArgumentList "SeuComando"

# executa um script com outra credencial solicitada
# Start-Process -FilePath "powershell" -ArgumentList "-File 'C:\Caminho\Para\SeuScript.ps1'" -Credential (Get-Credential) -NoNewWindow

# executa um comando com a credencial configurada
# $credential = New-Object System.Management.Automation.PSCredential($username, $password)
# Start-Process powershell -Credential $credential -ArgumentList "SeuComando"

# permissão de execução de scripts
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# executa o script
# & "\\10.8.32.3\arquivos\Arquivos curso superior\tads-algoritmos\02-instalando-ambiente-python.ps1"


# executa os scripts com a credencial configurada
# $credential = New-Object System.Management.Automation.PSCredential($username, $password)
# Start-Process -FilePath "powershell" -ArgumentList "-File '\\10.8.32.3\arquivos\Arquivos curso superior\tads-algoritmos\03-preparando-ambiente-python.ps1'" -Credential $credential -NoNewWindow
# Start-Process -FilePath "powershell" -ArgumentList "-File '\\10.8.32.3\arquivos\Arquivos curso superior\tads-algoritmos\04-baixando-prova.ps1'" -Credential $credential -NoNewWindow
