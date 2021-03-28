import sqlite3

conn=sqlite3.connect("C:/Users/qkreh/Desktop/AlgorithmStudy/python_study/resource/database.db")
c=conn.cursor()

# c.execute("UPDATE users SET phone=? WHERE id=?",('010-0000-0000', 1))
# conn.commit()

for line in c.execute("SELECT * FROM users"):
    print(line)
for i in range(1,4):
    c.execute("DELETE FROM users WHERE id=?",(i,))
print("-----------")
for line in c.execute("SELECT * FROM users"):
    print(line)
print(c.execute("DELETE FROM users").rowcount)
for line in c.execute("SELECT * FROM users"):
    print(line)