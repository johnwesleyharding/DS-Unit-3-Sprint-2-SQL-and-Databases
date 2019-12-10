
import sqlite3
import pandas as pd

def query(q, db = sqlite3.connect('rpg_db.sqlite3')):
    cursor = db.cursor()
    result = cursor.execute(q).fetchall()
    cursor.close()
    db.commit()
    print(result)
    return result

# PART 1
# How many total Characters are there?
resultc = query('SELECT COUNT (*) FROM charactercreator_character;')
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



# On average, how many Items does each Character have?
result = query('SELECT COUNT (*) FROM charactercreator_character_inventory;')
print(f'{round(result[0][0] / resultc[0][0], 2)} average items per character')

# On average, how many Weapons does each character have?

# print(f'{resultw[0][0] / resultc[0][0]} average weapons per character')


# PART 2
df = pd.read_csv('buddymove_holidayiq.csv')


