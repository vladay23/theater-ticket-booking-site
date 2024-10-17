import psycopg2

conn = None
try:
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host = 'localhost',
        dbname = 'test',
        user = 'postgres',
        password = '123456',
        port = 5432
    )

    cur = conn.cursor()
    print('Connected to the PostgreSQL database')
    cur.close()

except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
