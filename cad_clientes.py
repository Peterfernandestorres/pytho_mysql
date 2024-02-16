import mysql.connector as mc

# Estabelecer s conexao com o banco
cx = mc.connect (
    host="127.0.0.1",
    port="3784",
    user="root",
    password="808",
    database="banco"
)

# Verificar se a conexao foi estabelecida
print (cx)

# Criação de variaveis para usuario passar os dados do cliente para cadastrar
nome = input ("Digite o Nome do Cliente: ")
email = input ("Digite o email do Cliente: ")
telefone = input ("Digite o Numero de Telefone do Cliente: ")

cursor = cx.cursor ()
cursor.execute ("Insert into clientes (nome_cliente,email,telefone)values('"+nome+"','"+email+"','"+telefone+"')")