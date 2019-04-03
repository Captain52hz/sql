import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO inventory VALUES('Fords', 'Aes', 1001)")
	c.execute("INSERT INTO inventory VALUES('Fords', 'Mcd', 1000)")
	c.execute("INSERT INTO inventory VALUES('Fords', 'Scl', 2000)")
	c.execute("INSERT INTO inventory VALUES('Hondas', 'Boa', 1005)")
	c.execute("INSERT INTO inventory VALUES('Hondas', 'Sol', 1007)")
