# # SELECT statement
# import sqlite3

# with sqlite3.connect("new.db") as connection:
# 	c = connection.cursor()
# 	for row in c.execute("SELECT firstname, lastname from employees"):
# 		print(row)


# import sqlite3

# with sqlite3.connect("new.db") as connection:
# 	c = connection.cursor()
# 	c.execute("SELECT firstname, lastname from employees")
# 	rows = c.fetchall()
# 	for r in rows:
# 		print(r[0], r[1])

#UPDATE and DELETE statements
import sqlite3
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("UPDATE population SET population = 9000000 WHERE city='New York City'")
	c.execute("DELETE FROM population WHERE city='Boston'")
	print("\nNEW DATA:\n")
	c.execute("SELECT * FROM population")
	rows = c.fetchall()
	for r in rows:
		print(r[0], r[1], r[2])
