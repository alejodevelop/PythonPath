import mysql.connector
conn = mysql.connector.connect( host='localhost', user='alejo', password='1234', db='ciclo3db')
cur = conn.cursor()
# ejemplo de como hacer una peticion a la base de datos por medio de un query
# cur.execute("SELECT nombre, id FROM tabla") 
conn.close()

