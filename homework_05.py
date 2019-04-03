import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE orders (make TEXT, model TEXT, order_date DATE)")

	orderinfos = [
				('Fords', 'Aes', '2001-02-06'),
				('Fords', 'Mcd', '2011-12-09'),
				('Fords', 'Scl', '2004-09-28'),
				('Hondas', 'Boa', '2009-05-07'),
				('Hondas', 'Sol', '2000-01-01'),
				('Fords', 'Aes', '2011-12-06'),
				('Fords', 'Mcd', '2006-10-09'),
				('Fords', 'Scl', '2003-03-28'),
				('Hondas', 'Boa', '2007-05-02'),
				('Hondas', 'Sol', '2008-04-01'),
				('Fords', 'Aes', '2009-06-06'),
				('Fords', 'Mcd', '2016-11-29'),
				('Fords', 'Scl', '2005-09-24'),
				('Hondas', 'Boa', '2002-09-27'),
				('Hondas', 'Sol', '2010-01-21')
				]
	c.executemany('INSERT INTO orders VALUES(?, ?, ?)', orderinfos)