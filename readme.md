# conexão do Python com o MYSQL

!["IMAGEM PYTHON COM MYSQL"] (https://miro.medium.com/v2/resize:fit:1358/1*5PSjhz9Xx-4cj4Dz2FrHkA.jpeg)

## Drive de Comunicações com o Mysql
para estabelecer a comunicação entre Python e o banco de dados mysql,
iremos usar o seguinte drive:
<a href="></a>

### Comando para Instalar Drive
---python
   python -m pip install mysql-connector-python
---

### Configuração do Banco de Dados MYSQL
O nosso Banco de dados está em um conteiner de docker. para acessa-lo será necessário criar o
container, então faremos os seguintes Comandos em um servidor Fedora com o docker instalado:

### Criação de Volume
```shell
mkdir dadosclientes
```

#### Criação do Container
```shell
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=808 -d mysql^C
```

# Criação do Banco de Dados e da tabela de clientes
```sql
CREATE DATABASE banco;
CREATE TABLE clientes(
clientes_id int auto_increment primary key,
nome_cliente varchar(50) not null,
email varchar(100) not null unique,
telefone varchar(20)
)

```
### arquivo de Cadrastro: cad_clientes.py

```python
import mysql.connector as mc

# Estabelescer a Conexao com o banco
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="808",
    database="banco"
)
```
### Arquivo de atualização: up_clientes.py
```python
import mysql.connector as mc

cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="808",
    database="banco"
)

cursor = cx.cursor ()
cursor.execute ("Select * from clientes")
for i in cursor:
    print (i)

print ("O Que Você deseja Atualizar ?, Digite: ")
print ("1 - Para Nome")
print ("2 - Para email")
print ("3 - Para Telefone")
op = input ("Digite a Opção Desejada: ")
id = input ("Agora, Digite seu Id Do Cliente: ")
dado = input ("Digite a Nova Informação: ")
if (op=="1"):
    cursor.execute ("update clientes set nome_cliente='"+dado+"' where clientes_id="+id)
elif (op=="2"):
    cursor.execute ("update clientes set email='"+dado+"' where clientes_id="+id)
elif (op=="3"):
    cursor.execute ("update clientes set telefone='"+dado+"' where clientes_id="+id)
else:
    print ("Opção Invalida ! Tente Novamente")

cx.commit ()
