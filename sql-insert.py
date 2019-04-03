# 创建一个数据库
# 为他一个表
# 用for插入100个随机数字
import sqlite3
from random import randint

conn = sqlite3.connect("newnum.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE newnum(num INT)")

for i in range(100):
	cursor.execute("INSERT INTO newnum VALUES(?)", (randint(0, 100),))

conn.commit()
conn.close()
