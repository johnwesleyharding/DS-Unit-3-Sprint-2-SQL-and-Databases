
import sqlite3
import pandas as pd


# PART 1 ------------------------------------- Notebook code more recent
def query(q, db = sqlite3.connect('rpg_db.sqlite3')):
    cursor = db.cursor()
    cursor.execute(q)
    result = cursor.fetchall()
    cursor.close()
    db.commit()
    return result

# How many total Characters are there?
q = "SELECT COUNT (*)\
     FROM charactercreator_character;"
resultc = query(q)
print(f'{resultc[0][0]} total characters.')

# How many of each specific subclass?
result = query('SELECT COUNT (*) FROM charactercreator_fighter;')
print(f'{result[0][0]} fighters.')

result = query('SELECT COUNT (*) FROM charactercreator_cleric;')
print(f'{result[0][0]} clerics.')

result = query('SELECT COUNT (*) FROM charactercreator_thief;')
print(f'{result[0][0]} thieves.')

result = query('SELECT COUNT (*) FROM charactercreator_mage;')
resultn = query('SELECT COUNT (*) FROM charactercreator_necromancer;')
print(f'{result[0][0]} mages including {resultn[0][0]} necromancers.')

# How many total Items?
resulti = query('SELECT COUNT (*) FROM armory_item;')
print(f'{resulti[0][0]} total items.')

# How many of the Items are weapons? How many are not?
resultw = query('SELECT COUNT (*) FROM armory_weapon;')
print(f'{resultw[0][0]} weapons, {resulti[0][0] - resultw[0][0]} other items.')

# How many Items does each character have? (Return first 20 rows)
result = query('SELECT COUNT(character_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;')
for i in range(len(result)):
    print(f'Character ID: {i + 1} has {result[i][0]} items.')

# How many Weapons does each character have? (Return first 20 rows)
result = query('SELECT cc.character_id as ID, cc.name as person, count(aw.power) as weapons FROM charactercreator_character as cc, charactercreator_character_inventory as cci, armory_weapon as aw WHERE cc.character_id = cci.character_id AND aw.item_ptr_id = cci.item_id GROUP BY cc.character_id ORDER BY weapons DESC, person LIMIT 20;')
for i in range(len(result)):
    print(f'{result[i][1]} has {result[i][2]} weapons.')

# On average, how many Items does each Character have?
result = query('SELECT COUNT (*) FROM charactercreator_character_inventory;')
print(f'{round(result[0][0] / resultc[0][0], 2)} average items per character')

# On average, how many Weapons does each character have?

result = query('SELECT COUNT(*) FROM charactercreator_character_inventory as cci, armory_weapon as aw WHERE cci.item_id = aw.item_ptr_id;')
print(f'{round(result[0][0] / resultc[0][0], 2)} average weapons per character')


# PART 2 -------------------------------------
def query(q, db = sqlite3.connect('buddymove_holidayiq.sqlite3')):
    cursor = db.cursor()
    cursor.execute(q)
    result = cursor.fetchall()
    cursor.close()
    db.commit()
    return result

# Open a connection to a new (blank) database file buddymove_holidayiq.sqlite3
db = sqlite3.connect('buddymove_holidayiq.sqlite3')

# Use df.to_sql (documentation) to insert the data into a new table review in the SQLite3 database
df = pd.read_csv('buddymove_holidayiq.csv')
df.to_sql('review', db)

# Count how many rows you have - it should be 249!
result = query('SELECT COUNT(*) FROM review;'')
print(f'{result[0][0]} rows.')

# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
result = query('SELECT COUNT(*) FROM review WHERE Nature >= 100 AND Shopping >= 100;')
print(f'{result[0][0]} users are interested in nature and shopping.')

# (Stretch) What are the average number of reviews for each category?
for category in ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']:
    q = f'SELECT AVG({category}) FROM review;'
    result = query(q)
    print(f'Average interest in {category}: {round(result[0][0])}')
