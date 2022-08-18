import sqlite3

"""
Агрегирующие ф-ии: 

GROUP BY - ключевое слово для агрегации данных (группирует по одинаковому значению столбца)
COUNT() - используется для агрегации строк и возвращает кол-во записей
SUM() - считает сумму всех значений из столбца
AVG()
MIN()
MAX()
"""
""" as - ключевое слово для обозначения псевдонима имени столбца
    distinct - уникальные значения
"""

""" HAVING - аналогичен оператору WHERE за тем исключением,
    что применяется не для всего набора столбцов таблицы, 
    а для набора созданного оператором GROUP BY и применяется всегда строго после него

ORDER BY - сортировка
    asc, desc - от меньшего к большему и от большего к меньшему"""

query_1 = 'select * from netflix'

"""count() - ф-ия подсчитывает кол-во строк"""
"""group by - группирует по одинаковому значению в столбце"""
query_2 = """
            select release_year, count(title)
            from netflix
            group by release_year
            """

"""distinct - уникальные значения"""
query_3 = """
            select count(distinct director)
            from netflix
            """

"""Таким образом count() позволяет высчитавать кол-во строк приходящихся на конкретную группу"""
query_4 = """
            select count(country), country
            from netflix
            where country != ''
            group by country
            """

query_5 = """
            select min(release_year), country
            from netflix 
            group by country
            order by min(release_year)
            """

"""min(), max(), avg() - минимальное, максимальное, среднее значение столбца"""
query_6 = """
            select min(release_year), max(release_year), avg(release_year)
            from netflix
            """

query_7 = """
            select type, country, avg(duration)
            from netflix
            group by type, country
            """

"""sum() - считает сумму значений столбца"""
"""query_8 - выведет суммы минут всех фильмов для каждого года"""
query_8 = """
            select release_year, type, sum(duration)
            from netflix
            where duration_type = 'min'
            group by release_year
            """

"""query_9 - выведет суммы минут всех фильмов для каждой страны"""
query_9 = """
            select country, sum(duration)
            from netflix
            where type = 'Movie'
            group by country
            order by sum(duration)
            """

""" as - ключевое слово для обозначения псевдонима имени столбца"""
""" asc, desc - от меньшего к большему и от большего к меньшему"""
query_10 = """
            select country, sum(duration) as total_duration
            from netflix
            where type = 'TV Show' and country != ''
            group by country
            order by total_duration desc
            """

""" HAVING - фильтрация по результатам агрегации и группировки"""
query_11 = """
            select country, sum(duration) as total_duration
            from netflix
            where type = 'TV Show' and country != ''
            group by country
            having total_duration between 2 and 10
            order by total_duration desc
            """

"""query_12 - выведет количество тв шоу и фильмов в странах которых присутствует Индия"""
query_12 = """
                select type, count(title)
                from netflix
                where country like '%India%'
                group by type
                """

with sqlite3.connect('netflix.db') as connection:
    cursor = connection.cursor()
    cursor.execute(query_11)
    result = cursor.fetchall()

for row in result:
    print(row)
