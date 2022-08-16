import sqlite3

query = """
        select title
        from netflix
        where country=:country_1
"""

country_1 = 'Russia'

with sqlite3.connect('netflix.db') as connection:
    cursor = connection.cursor()
    result = connection.execute(query, {'country_1': country_1})
    connection.commit()
    for row in result:
        print(dict(row))
