########## Acesso ao FTP usando a lib PARAMIKO https://www.paramiko.org/
import paramiko
import sys
import datetime

####| CREDENCIAIS DE ACESSO |####
HOST = "ftp.dlptest.com"
USER = "dlpuser"
SENHA = "rNrKYTX9g7z3RgJRmxWuGHbeu"
##### essa senha muda de tempos em tempos. acessar https://dlptest.com/ftp-test/ para conferir a senha atual


####| PASTAS E ARQUIVO: ORIGEM e DESTINO |####
dataHoje = datetime.datetime.now()
dataOntem = dataHoje - datetime.timedelta(days=1)

pastaDestino = "C:/pastadestino/"
pastaFtp = "/home/pastaorigemftp/"
arq = "NOME_ARQUIVO_" + dataOntem.strftime('%d_%m_%Y') ##o nome do arquivo muda dependendo do dia que o ftp for acessado
extArq = ".csv"
####

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=HOST,username=USER,password=SENHA,allow_agent=False,look_for_keys=False)
    sftp = client.open_sftp()
    print('Conexão realizada com sucesso!\nBuscando arquivos:\n - ', arq+extArq)
except:
    print('\nOps ... tivemos um problema!\nErro na conexão: verifique as credenciais de acesso.')
    sys.exit()
####

####| DOWNLOADS DO .CSV |####
try:
    sftp.get(pastaFtp+arq+extArq,pastaDestino+arq+extArq)
    print('Arquivo',arq+extArq,' baixado com sucesso!')
    sftp.close()
except:
    print('Ops ... tivemos um problema!')
    print("\nArquivo: ",pastaDestino,arq+extArq+" não encontrado!")
    sys.exit()