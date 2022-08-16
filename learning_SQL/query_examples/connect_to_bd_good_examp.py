import sqlite3

query = """
        select title, country, max(release_year) as max_year
        from netflix
        where country like '%Russia%'
"""

with sqlite3.connect('netflix.db') as connection:
    """этот способ вернет список кортежей"""
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result, '\n')

with sqlite3.connect('netflix.db') as connection:
    """этот способ вернет список объектов, которые можно привести к словарю вида {column_name: value}"""
    connection.row_factory = sqlite3.Row
    result = connection.execute(query).fetchall()
    print(result)
    for row in result:
        print(dict(row))
