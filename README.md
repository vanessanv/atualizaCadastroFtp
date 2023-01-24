# atualizaCadastroFtp

## Paramiko
A lib usada para fazer o download dos arquivos via SFTP foi a Paramiko. A documentação pode ser encontrada aqui:
https://www.paramiko.org/

Essa biblioteca serve basicamente para implementação do protocolo SSHv2 através do Python. Neste código usarei apenas o comando de download mas outras opções também estão disponíveis, basta consultar a documentação.

## Para testar a conexão FTP
Para testar a conexão via ftp eu usei um site público que disponibiliza um FTP para testes. As configurações para funcionamento estão aqui: 
https://dlptest.com/ftp-test/

* Todo upload feito para esse FTP fica disponível apenas por 10 minutos após isso os arquivos são apagados.
* A senha para acessar esse FTP de teste muda com bastante frequência, não esquecer de atualizar antes de fazer o teste.

## Para executar o código
Para esse código funcionar é necessário fazer alterações nas variáveis:
* SENHA - senha de acesso ao FTP
* HOST e USER - se não for usar o FTP de teste
* pastaDestino - onde você quer que o download seja realizado
* pastaFtp - pasta/caminho do FTP de onde virá o arquivo que será baixado 
* arq - nome do arquivo
* extArq - qual a extensão do arquivo que será baixado

Neste exemplo eu usei uma data como parte do nome do arquivo e ela pode ser removida sem problemas caso não tenha necessidade.
