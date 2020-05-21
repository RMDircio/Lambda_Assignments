import sqlite3

#  1) How many total characters are there? 279
SELECT COUNT(DISTINCT name) from charactercreator_character
# to find unique values of names
SELECT name, count(*) from charactercreator_character GROUP BY name 

# 2) How many of each specific subclass?
```Cleric``` # 75
SELECT COUNT(DISTINCT character_ptr_id) FROM charactercreator_cleric

```Fighter``` # 68
SELECT COUNT(DISTINCT character_ptr_id) FROM charactercreator_fighter
``` Mage``` # 108
SELECT COUNT(DISTINCT character_ptr_id) FROM charactercreator_mage
```Necromancer``` # 11
SELECT COUNT(DISTINCT mage_ptr_id) FROM charactercreator_necromancer
```Thief``` # 51
SELECT COUNT(DISTINCT character_ptr_id) FROM charactercreator_thief

# 3) How many total items?
```Total items + weapons``` #  172 
SELECT COUNT(DISTINCT name) FROM armory_item
# add these two total together for all items
```Total Weapons``` # 37
SELECT COUNT(DISTINCT item_ptr_id) FROM armory_weapon

# 4) How many of the Items are weapons? 
```How many are not?```` # 37
SELECT COUNT(DISTINCT item_ptr_id) FROM armory_weapon

# 5) How many Items does each character have? (Return first 20 rows)
SELECT 
	character_id,
	count(*)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20

# 6) How many Weapons does each character have? (Return first 20 rows)

# 7) On average, how many Items does each Character have?

# 8) On average, how many Weapons does each character have?




