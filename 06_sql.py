import sqlite3


with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	sql = {
       'Average': "SELECT avg(population) FROM population",
       'Count': "SELECT count(population) FROM population",
       'Max': "SELECT max(population) FROM population",
       'Min': "SELECT min(population) FROM population",
       'Sum': "SELECT sum(population) FROM population"
      }
	for key, value in sql.items():
		c.execute(value)
		result = c.fetchone()
		print(key + ":", result[0])