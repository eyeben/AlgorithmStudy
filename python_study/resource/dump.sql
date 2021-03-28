BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'park','eyeben#naver.com','010-1234-1234','kim.com','2021-03-25 16:32:05');
INSERT INTO "users" VALUES(2,'tee','asf@naver.com','010-1234-2134','tee.com','2021-03-25 17:55:21');
INSERT INTO "users" VALUES(3,'lee','asf@naver.com','010-1234-2134','lee.com','2021-03-25 17:55:21');
COMMIT;
