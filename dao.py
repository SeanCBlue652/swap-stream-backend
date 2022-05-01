import psycopg2
import databasePasswordDecryption
import json

DATABASE_NAME = "postgres"
DATABASE_USER = "swapstreamAdmin"
DATABASE_HOST = "swapstreamdb.ck8zwecvtffz.us-east-2.rds.amazonaws.com"
DATABASE_PORT = "5432"
DATABASE_PASSWORD = databasePasswordDecryption.getDBPassword()


def get_test_data():
    conn = None
    try:
        conn = psycopg2.connect(
            host=DATABASE_HOST,
            database=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD)

        cur = conn.cursor()
        cur.execute('SELECT * FROM "userdata"."users"')
        users = cur.fetchall()
        cur.close()
        output = dict()
        for user in users:
            output[user[0]] = user
        return output
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return {"Error": str(error)}
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def add_user(user_id, user_name, service):
    conn = psycopg2.connect(
        host=DATABASE_HOST,
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD)
    cur = conn.cursor()
    sql = f"INSERT INTO userdata.users(user_id, username, services) VALUES({user_id}, '{user_name}', '{service}');"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def formatUsers(results):
    item = results[0]
    retval = dict()
    retval['name'] = item[0]
    return retval

def get_user(user_id):
    conn = psycopg2.connect(
        host=DATABASE_HOST,
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD)
    cur = conn.cursor()
    sql = f"SELECT username FROM userdata.users WHERE user_id = {user_id}"
    cur.execute(sql)
    results = cur.fetchall()

    return formatUsers(results)

def add_playlist(plist_id, user_id, title, service, owner):
    conn = psycopg2.connect(
        "dbname=postgres user=postgres host=127.0.0.1 port=5432"
    )
    cur = conn.cursor()
    sql = f"INSERT INTO playlists(plist_id, user_id, title, service, owner) VALUES({plist_id}, {user_id}, {title}, {service}, {owner});"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def add_song(title, artist, service, url, index, plist_id):
    conn = psycopg2.connect(
        host=DATABASE_HOST,
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD
    )
    cur = conn.cursor()
    sql = f"INSERT INTO songs(title, artist, service, url, index, plist_id) VALUES({title}, {artist}, {service}, {url}, {index}, {plist_id});"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def make_dict(results: list) -> dict:
    my_dict = dict()
    

    return my_dict


def get_playlist_by_user(user_id):
    conn = psycopg2.connect(
        host=DATABASE_HOST,
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD
    )
    cur = conn.cursor()
    sql = f"SELECT songs FROM userdata.playlists, userdata.users WHERE playlists.user_id = {user_id} AND users.user_id=playlists.user_id"
    cur.execute(sql)
    results = cur.fetchall()
    ''' insert subroutine to sort it into proper dictionary'''
    return results

def format_playlists(results):
    item = results[0]
    retval = dict()
    info = dict()
    entry = list()
    piece = dict()
    piece['name'] = item[0]
    piece['id'] = item[1]
    piece['service'] = item[2]
    entry.append(piece)
    info['info'] = entry
    info['image'] = item[5]
    info['profile_image'] = item[6]
    song_list = list()
    song_list.append(item[3])
    song_list.append(info)
    song_list += item[4]['songs']
    retval['playlists'] = song_list 
    return retval

def get_playlist_by_id(plist_id, user_id):
    conn = psycopg2.connect(
        host=DATABASE_HOST,
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD
    )
    cur = conn.cursor()
    sql = f"SELECT DISTINCT username, users.user_id, services, playlists.name, songs, image, pfp FROM userdata.playlists, userdata.users WHERE plist_id = {plist_id} AND userdata.users.user_id = userdata.playlists.user_id AND userdata.users.user_id = {user_id}"
    print(sql)
    cur.execute(sql)
    results = cur.fetchall()
    


    return format_playlists(results)

def store_playlist(plist_id: int, user_id: int, songs: dict, name: str, image: str):
    conn = psycopg2.connect(
        host=DATABASE_HOST,
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD
    )
    cur = conn.cursor()
    insertion = json.dumps(songs)
    sql = f"INSERT INTO userdata.playlists(plist_id, user_id, songs, name, image) VALUES({plist_id},{user_id}, '{insertion}','{name}','{image}');"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

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

