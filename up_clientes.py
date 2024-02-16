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
