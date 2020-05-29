import os
import json
import sqlite3
import psycopg2
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from psycopg2.extras import DictCursor
from psycopg2.extras import execute_values

load_dotenv()

# change type for int4 error
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

###
# Read in passenger data from CSV file
###

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), 'titanic.csv')

titanic_df = pd.read_csv(CSV_FILEPATH)
print(titanic_df.head())
print(titanic_df.dtypes)



###
# Connect to the PostgreSQL database
###

DB_NAME = os.getenv('DB_NAME', default = 'try again')
DB_USER = os.getenv('DB_USER', default = 'try again')
DB_PASSWORD = os.getenv('DB_PASSWORD', default = 'try again')
DB_HOST = os.getenv('DB_HOST', default = 'try again')

connection = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST)

# A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()

##
# Create table to store passengers
##
    
create_sql_table = """
DROP TABLE IF EXISTS ship_passengers;
CREATE TABLE IF NOT EXISTS ship_passengers (
    id SERIAL PRIMARY KEY,
    "survived" int4,
    "pclass" int4,
    "name" text,
    "sex" text,
    "age" int4,
    "sibling_spouse_count" int4,
    "parent_child_count" int4,
    "fare" float8
);
"""

cursor.execute(create_sql_table)

##
# Insert passenger data
##

insertion_query = f'''
INSERT INTO ship_passengers (
    survived,
    pclass,
    name,
    sex,
    age,
    sibling_spouse_count,
    parent_child_count,
    fare)
    VALUES %s
'''

# covert df to list of tuples
list_of_tuples = list(titanic_df.to_records(index=False))

execute_values(cursor, insertion_query, list_of_tuples)


##
# Last steps to complete/commit/close
##

connection.commit()

cursor.close()
connection.close()



