import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	cities = [
			('Boston', 'MA', 600000),
			('Chicago', 'TX', 2700000),
			('Houston', 'AZ', 1500000)
			]
	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)