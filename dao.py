from typing import Optional
import psycopg2

def get_test_data():
    conn = psycopg2.connect(
        "dbname=postgres user=postgres host=127.0.0.1 port=5432"
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM "users"')
    output = dict()
    user = cur.fetchall()
    for each in user:
        output[each[0]] = each
    return output


def get_userdata():
    try:
        conn = psycopg2.connect(
            host="swapstream-dev.ck8zwecvtffz.us-east-2.rds.amazonaws.com",
            database="postgres",
            user="swapstreamAdmin",
            password="XcLusU7pvLI2PO6ywDYS")

        cur = conn.cursor()
        cur.execute('SELECT * FROM "userdata"."users"')
        user = cur.fetchone()
        cur.close()
        print('Database connection closed.')
        return {"User": str(user)}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return {"Error": str(error)}
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')