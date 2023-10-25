import sqlite3
import random


class DataBase():
    
   
    
    def init_db():
        with sqlite3.connect("app\\database\\posts.db") as conn:
            cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXiSTS Posts (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title   TEXT    NOT NULL,
    content TEXT    NOT NULL
                            )""")
    def get_all_posts():
        with sqlite3.connect("app\\database\\posts.db") as conn:
            cursor = conn.cursor()
        all_posts = cursor.execute("""SELECT * FROM Posts""").fetchall()
        #print(all_posts)
        
        s = []
        for text in all_posts:
            data = {}
            print(text)
            data['title'] = text[1]
            data['content'] = text[2]
            data['id'] = text[0]
            s.append(data)
        print(s)
        return s
        
    def test_db(title, content):
        conn = sqlite3.connect("app\\database\\posts.db")
        cursor = conn.cursor()
        id = len(cursor.execute("""SELECT * FROM Posts""").fetchall())
        cursor.execute("""INSERT INTO Posts VALUES (?, ?, ?)""", (id, title, content,))
        conn.commit()
        conn.close()        

    def add_posts(title, content):
        with sqlite3.connect("app\\database\\posts.db") as conn:
            cursor = conn.cursor()
            id =len(cursor.execute("""SELECT post_id FROM Posts""").fetchall())+1
            cursor.execute("""INSERT INTO Posts VALUES (?, ?, ?) """, (id, title, content,))
            

    
DataBase.get_all_posts()



