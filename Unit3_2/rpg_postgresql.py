'''
Importing a Sqlite3 database into a PostgreSQL database
'''

import os
import sqlite3
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_NAME = os.getenv('DB_NAME', default = 'try again')
DB_USER = os.getenv('DB_USER', default = 'try again')
DB_PASSWORD = os.getenv('DB_PASSWORD', default = 'try again')
DB_HOST = os.getenv('DB_HOST', default = 'try again')

# get sqlite3 file
SQLITE3_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")
connection = sqlite3.connect(SQLITE3_FILEPATH)
connection.row_factory = sqlite3.Row
print('CONNECTION:', connection)

cursor = connection.cursor()
print('CURSOR', cursor)


rpg_df = pd.read_sql('SELECT * FROM charactercreator_character', connection)

sql_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
engine = create_engine(sql_url)

rpg_df.to_sql('rpg_data', engine, if_exists='replace')

connection.commit()

cursor.close()
connection.close()








