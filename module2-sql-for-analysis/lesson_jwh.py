
import sqlite3
import psycopg2

dbname = 'wgloisnl'
user = 'wgloisnl'
password = 'LSM5PtNxZhMfbVGPuIx3y4hsFEf42cuz'
host = 'echo.db.elephantsql.com'

db0 = sqlite3.connect('rpg_db.sqlite3')
db1 = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)

c1 = db1.cursor()

# c1.execute('select * from test_table;')
# result = c1.fetchall()
# print(result)

def liteq(q, db = sqlite3.connect('rpg_db.sqlite3')):
    cursor = db.cursor()
    result = cursor.execute(q).fetchall()
    cursor.close()
    db.commit()
#     print(result)
    return result

def pgqr(q, db = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)):
    cursor = db.cursor()
    cursor.execute(q)
    result = cursor.fetchall()
    cursor.close()
    db.commit()
#     print(result)
    return result

def pgq(q, db = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)):
    cursor = db.cursor()
    cursor.execute(q)
    cursor.close()
    db.commit()

resultc = liteq('SELECT * from charactercreator_character;')
print(resultc[0][:])
print(resultc[-1][:])

resultp = liteq('PRAGMA table_info(charactercreator_character);')
for row in resultp:
    print(row)

# pgq('create table charactercreator_character (character_id SERIAL PRIMARY KEY, name varchar(30), level integer, exp integer, hp integer, strength integer, intelligence integer, dexterity integer, wisdom integer);')

# pgqr('select * from pg_catalog.pg_tables WHERE schemaname != "pg_catalog" AND schemaname != "information_schema";') HELP

# exinsert = """
# insert into charactercreator_character
# (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
# values """ + str(characters[0][1:] + ';')

for row in resultc:
    pgq('insert into charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom) values ' + str(row[1:]) + ';')

resultpc = pgqr('SELECT * from charactercreator_character;')
print(resultpc[0][:])
print(resultpc[-1][:])
