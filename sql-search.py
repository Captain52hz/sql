import sqlite3
print("perform an aggregation?")
sql = {
       '1': "SELECT avg(num) FROM newnum",
       '2': "SELECT max(num) FROM newnum",
       '3': "SELECT min(num) FROM newnum",
       '4': "SELECT sum(num) FROM newnum"
      }
while True:
	p = input("AVG: 1,	MAX: 2, MIN: 3, SUM: 4, exit: 0\n")
	if not isinstance(p, int) or int(p)==0 or int(p)>4:
		exit()
	with sqlite3.connect("newnum.db") as connection:
		c = connection.cursor()
		c.execute(sql[p])
		r = c.fetchone()
		print({'1': 'AVG',	'2': 'MAX', '3': 'MIN', '4': 'SUM'}[p] + ":" + str(r[0]))