import sqlite3  
  
con = sqlite3.connect("comments.db")  
db=con.cursor()

#contact Data table to hold name , mail , message
#db.execute("create table contact (name TEXT PRIMARY KEY NOT NULL, mail text NOT NULL,message text NOT NULL)")
#db.execute("insert into contact values ('uk','kd@gmail.com','best')")
#print('done')
#db.execute("select * from contact")
#db.execute('drop table contact')
db.execute("create table comments (name TEXT PRIMARY KEY , mail text ,message text )")
db.execute("insert into comments values ('uk','kd@gmail.com','best')")
con.close()  