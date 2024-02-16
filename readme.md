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