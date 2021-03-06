import sqlite3

with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()

	c.execute("SELECT * FROM inventory")
	rows = c.fetchall()
	for r in rows:
		print(r[0], r[1], "\n", r[2])
		print(r[2])
		c.execute("SELECT count(order_date) FROM orders WHERE make=? and model=?", \
                  (r[0], r[1]))
		results = c.fetchone()
		print(results[0])
