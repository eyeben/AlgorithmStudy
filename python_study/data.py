import sqlite3
import datetime
import pandas

now =datetime.datetime.now()
print("now : ", now)

nowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version : ', sqlite3.sqlite_version)

conn = sqlite3.connect('C:/Users/impjt/OneDrive/바탕 화면/AlgorithmStudy/python_study/resource/database.db', isolation_level=None)
c= conn.cursor()

#데이터 생성타입은 TEXT, NUMERIC,INTEGER, REAL, BLOB
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# c.execute("INSERT INTO users VALUES(1,'park','eyeben#naver.com','010-1234-1234','kim.com',?)",(nowDatetime,))
# c.execute("INSERT INTO USERS(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", ("sadf","sadf"....))

userList = (
    (3, 'lee', 'asf@naver.com', '010-1234-2134','lee.com', nowDatetime),
    (2, 'tee', 'asf@naver.com', '010-1234-2134','tee.com', nowDatetime),
    (1, 'eee', 'asf@naver.com', '010-1234-2134','eee.com', nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",userList)
