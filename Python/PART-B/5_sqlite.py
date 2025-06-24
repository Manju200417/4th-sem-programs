# 5. Create SQLite Database and Perform Operations on Tables 
# import os
import sqlite3
db = sqlite3.connect('data.db')
db.execute("create table if not exists students (id int, name text, age int)")
db.execute("insert into students values (1, 'Ravi', 21)")
db.commit()
for row in db.execute("select * from students"):
    print(row)
db.close()


# if os.path.exists('data.db'):
#     os.remove('data.db')
#     print("Database file deleted.")