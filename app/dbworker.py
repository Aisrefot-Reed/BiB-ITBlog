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
        #LIMIT 10 OFFFSET :numOfPosts * 10 - 1
        # print(all_posts)
        s = []
        for text in all_posts:
            data = {}
        
            data['title'] = text[1]
            data['content'] = text[2]
            data['id'] = text[0]
            s.append(data)

        return list(reversed(s))
        
    def opened_post(post_id):
        conn = sqlite3.connect("app\\database\\posts.db")
        cursor = conn.cursor()
        post_data = {}
        pd = cursor.execute("""SELECT title, content FROM Posts WHERE post_id=?""",(post_id,) ).fetchall()
        post_data['content'] = pd[0][1]
        post_data['title'] = pd[0][0]
  
        conn.close()        
        return post_data
    
    def add_posts(title, content):
        with sqlite3.connect("app\\database\\posts.db") as conn:
            cursor = conn.cursor()
            id =len(cursor.execute("""SELECT post_id FROM Posts""").fetchall())+1
            cursor.execute("""INSERT INTO Posts VALUES (?, ?, ?) """, (id, title, content,))
            



# print(DataBase.opened_post(2))
# print(DataBase.get_all_posts(10))
