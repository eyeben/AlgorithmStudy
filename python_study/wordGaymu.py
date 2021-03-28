import random
import time
import winsound
import sqlite3
import datetime




# words=[]
# score=0
# with open('./resource/gaymufiru/word.txt','r') as f:
#     for word in f:
#         words.append(word.strip())

# input("press enter to start")
# start=time.time()
# for i in range(1,6):
#     q=random.choice(words)
#     typed=input("Q.%d\n%s\n" % (i,q))
#     if str(typed)==str(q):
#         winsound.PlaySound('./resource/gaymufiru/sound/good.wav',winsound.SND_FILENAME)
#         print("goody\n")
#         score+=1
#     else:
#         print("nopy\n")
#         winsound.PlaySound('./resource/gaymufiru/sound/bad.wav',winsound.SND_FILENAME)

# end=time.time()
# print("time: %.3f\nscore: %d"%(end-start,score))


conn=sqlite3.connect('./resource/gaymufiru/scoreboard1.db', isolation_level=None)
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scoreData(id INTEGER PRIMARY KEY AUTOINCREMENT, score INTEGER, time text, regdate text)")
datas={
    1:[1, 0.0, 0],
    2:[0, 0.0, 0],
    3:[0, 0.0, 0],
    4:[0, 0.0, 0],
    5:[0, 0.0, 0]
}

print((c.fetchall()))
if not len(c.fetchall()):
    for i in range(1,6):
        c.execute("INSERT INTO scoreData('id','score','time','regdate') VALUES(?,?,?,?)", (i, datas[i][0], datas[i][1], datas[i][2]))


