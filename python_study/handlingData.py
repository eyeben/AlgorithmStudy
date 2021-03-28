import sqlite3


conn = sqlite3.connect('C:/Users/qkreh/Desktop/AlgorithmStudy/python_study/resource/database.db', isolation_level=None)
c= conn.cursor()

# #조회
# param=(3,)
# c.execute("SELECT * FROM users WHERE id=?",param)
# print("param",c.fetchall())

# param2=2
# c.execute('SELECT * FROM users WHERE id="%s"' % param2)
# print(c.fetchone())

# c.execute('SELECT * FROM users WHERE id=:Id', {"Id":1})
# print(c.fetchall())

# param4=(1,3)
# c.execute("SELECT * FROM users WHERE id IN(%d,%d)" % (2,3))
# print(c.fetchall())

# c.execute("SELECT * FROM users WHERE id IN(?,?)",param4)
# print(c.fetchone())
# print(c.fetchone())
# print(type(c.fetchone()))
# print("---------")


# c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1":2,"id2":3})
# print(c.fetchall())

#DUMP
with conn:
    with open('C:/Users/qkreh/Desktop/AlgorithmStudy/python_study/resource/dump.sql','w') as f:
        for line in conn.iterdump():
            f.write('%s\n'%line)
        print("done")