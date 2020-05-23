import pandas as pd
import sqlite3

buddy_df = pd.read_csv(r'/home/regina/Documents/Lambda/Unit_3/Unit_3.2/Buddy_Move/buddymove_holidayiq.csv')
print(buddy_df.shape)
print(buddy_df.head())
print(buddy_df.isnull().sum())

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

cursor = conn.cursor()

buddy_df.to_sql('review', conn, if_exists = 'replace')

quest_query = {
    'How many rows are there?':
    '''SELECT
            COUNT(*)
        FROM
            review
        ;
    ''' ,
    'How many users reviewed at least 100 nature and at least 100 in shopping?':
    '''SELECT
            COUNT(*)
        FROM
            review
        WHERE
            Nature >= 100 
            AND Shopping >= 100
        ;
    ''' ,
    'What are the average reviews for each category?':
    '''SELECT
            AVG(Sports) AS Sports_Average, 
            AVG(Religious) AS Religion_Average,
            AVG(Nature) AS Nature_Average,
            AVG(Theatre) AS Theatre_Average,
            AVG(Shopping) AS Shopping_Average,
            AVG(Picnic) AS Picnic_Average
        FROM
            review
        ;
    '''
}

for i, q in enumerate(list(quest_query.keys())):
	result = cursor.execute(quest_query[q]).fetchall()
	print(f'Query {i} Question: {q}\nResults:')
	for row in result:
		print(row[:])
	print('\n')