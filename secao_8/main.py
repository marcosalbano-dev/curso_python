import psycopg2

conn = psycopg2.connect(dbname='sige', user='marcos.albano', password='Albano@1971', port='5432', host='172.28.1.160')
cursor = conn.cursor()

if cursor:
    print('Conexão OK!')


cursor.close()
conn.close()