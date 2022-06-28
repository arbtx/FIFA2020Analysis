import psycopg2

conn = psycopg2.connect(
    database = "EUPHEUS2020",
    user = "postgres",
    password = "eupheus",
    host = "localhost",
    port = "5432"
)

cur = conn.cursor()

cur.execute("select * from products2")
a = cur.fetchall()
print(a)