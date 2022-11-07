import psycopg2
from config import host, user, db_name


try:
   password = input("password:")
   connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
   connection.autocommit = True
   with connection.cursor() as cursor:
    cursor.execute("""create table all_info(id serial primary key, name varchar(500) NOT NULL, mark varchar(5));""")
    file = open('all_info.txt', 'r')
    for line in file:
        number, name, mark = line.split(' ')
        name = name.replace('-', ' ')
        cursor.execute(f"""INSERT INTO all_info (name, mark) VALUES ('{name}', '{mark}');""")
        print("[INFO] Inserting was succefully PostgreSQL")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        file.close()
        connection.close()
        print("[INFO] Close db in PostgreSQL")