import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("SELECT count(make) FROM orders WHERE model='Scl'")
	result = c.fetchone()
	print('Scl' + ':', result[0])