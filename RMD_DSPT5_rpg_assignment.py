import os
import sqlite3


DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'rpg_db.sqlite3')

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
print('CONNECTION:', connection)

cursor = connection.cursor()
print('CURSOR', cursor)

queries = [
'''
SELECT
	COUNT(DISTINCT name)
FROM
	charactercreator_character
;
''' ,
'''
SELECT
	name,
	COUNT(*)
FROM
	charactercreator_character
GROUP BY
	name
;
''' ,
'''
SELECT
	COUNT(DISTINCT character_ptr_id)
FROM
	charactercreator_cleric
;
''' ,
'''
SELECT 
	COUNT(DISTINCT character_ptr_id)
FROM 
	charactercreator_fighter
;
''' ,
'''
SELECT 
	COUNT(DISTINCT character_ptr_id) 
FROM
	charactercreator_mage
;
''' ,
'''
SELECT 
	COUNT(DISTINCT mage_ptr_id)
FROM 
	charactercreator_necromancer
;
''' ,
'''
SELECT
	COUNT(DISTINCT character_ptr_id)
FROM
	charactercreator_thief
;
''' ,
'''
SELECT
	COUNT(DISTINCT name)
FROM 
	armory_item
;
''' ,
'''
SELECT
	COUNT(DISTINCT item_ptr_id)
FROM
	armory_weapon
;
''' ,
'''
SELECT 
	character_id,
	count(*)
FROM 
	charactercreator_character_inventory
GROUP BY
	character_id
LIMIT 
	20
;
''' ,
'''
SELECT
	c.character_id
	,c.name as character_name
	,count(distinct w.item_ptr_id) as weapon_count
FROM 
	charactercreator_character as c
LEFT JOIN 
	charactercreator_character_inventory as inv ON c.character_id = inv.character_id
LEFT JOIN
	armory_weapon as w ON w.item_ptr_id = inv.item_id
GROUP BY 
	c.character_id
LIMIT
	20
;
''' ,
'''
SELECT
	AVG(item_counts.item_count)
FROM
	(
		SELECT 
		cci.character_id,
		COUNT(*) as item_count
		FROM charactercreator_character_inventory as cci
		GROUP BY cci.character_id
	) AS item_counts
;
''' ,
'''
SELECT
	AVG(weapon_count)
FROM
	(
	SELECT
		cci.character_id,
		COUNT(*) AS weapon_count
	FROM 
		charactercreator_character_inventory AS cci
		LEFT OUTER JOIN armory_weapon AS AW
		ON cci.item_id = AW.item_ptr_id
	WHERE 
		AW.item_ptr_id IS  NOT NULL
	GROUP BY
		cci.character_id
	)
;
''']

for i, q in enumerate(queries):
	result = cursor.execute(q).fetchall()
	print(f'Query {i} Results:')
	for row in result:
		print(row[:])
	print('\n')
