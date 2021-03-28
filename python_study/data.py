import sqlite3
import datetime

now =datetime.datetime.now()
print("now : ", now)

nowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version : ', sqlite3.sqlite_version)

conn = sqlite3.connect('C:/Users/qkreh/Desktop/AlgorithmStudy/python_study/resource/database.db', isolation_level=None)
c= conn.cursor()

#데이터 생성타입은 TEXT, NUMERIC,INTEGER, REAL, BLOB

c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# c.execute("INSERT INTO users VALUES(1,'park','eyeben#naver.com','010-1234-1234','kim.com',?)",(nowDatetime,))
# c.execute("INSERT INTO USERS(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", ("sadf","sadf"....))

c.execute("UPDATE users SET username=? WHERE id=?",('bee',2))
userList = (
    (1, 'lee', 'l@naver.com', '010-1234-2134','lee.com', nowDatetime),
    (2, 'tee', 't@naver.com', '010-1234-2134','tee.com', nowDatetime),
    (4, 'eee', 'e@naver.com', '010-1234-2134','eee.com', nowDatetime),
    (5, 'cee', 'c@naver.com', '010-1234-2134','tee.com', nowDatetime),
    (6, 'yee', 'y@naver.com', '010-1234-2134','eee.com', nowDatetime)
)
print(c.execute("DELETE FROM users").rowcount)
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

conn.commit