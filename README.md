import psycopg2
Suponemos que solamente podemos hacer consultas del tipo SELECT *
Queremos el join entre A(id int, nombre varchar(100)) y
B(id int, nombre varchar(100))
Reemplazar nombres de usuario y de la base de datos.
Ingresar otros parámetros si es necesario

conn = psycopg2.connect("dbname=XX user=XX")
curA = conn.cursor()
curB = conn.cursor()

curA.execute("SELECT * FROM A")
Supondremos que el id en ambas está en la posición 0.
Para hacerlo más elegante podemos obtener esa información del cursor.
Si queremos saber el orden de las columnas usamos el
atributo description del cursor:
print([column.name for column in curA.description])

tuplaA = curA.fetchone()
while tuplaA:
curB.execute("SELECT * FROM B")
tuplaB = curB.fetchone()
while tuplaB:
if tuplaA[0] == tuplaB[0]:
print("{} - {}".format(tuplaA, tuplaB))
tuplaB = curB.fetchone()
tuplaA = curA.fetchone()

conn.close()
