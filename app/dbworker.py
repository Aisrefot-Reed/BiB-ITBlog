import sqlite3
import random

database_file= "D:\\Programming\\languages\\PYTHON\\site-on-flask\\app\\database\\posts.db"

class DataBase():
    
    def init_db():
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Posts (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title   TEXT    NOT NULL,
    content TEXT    NOT NULL)""")
    def get_all_posts():
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
        all_posts = cursor.execute("""SELECT * FROM Posts""").fetchall()
        #LIMIT 10 OFFFSET :numOfPosts * 10 - 1
        # print(all_posts)
        s = []
        for text in all_posts:
            data = {}
            
            data['id'] = text[0]
            data['title'] = text[1]
            data['content'] = text[2]

            s.append(data)

        return list(reversed(s))
        
    def opened_post(post_id):
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()
        post_data = {}
        pd = cursor.execute("""SELECT title, content FROM Posts WHERE post_id=?""",(post_id,)).fetchall()
        post_data['content'] = pd[0][1]
        post_data['title'] = pd[0][0]
  
        conn.close()        
        return post_data
    
    def add_posts(title, content):
        with sqlite3.connect(database_file) as conn:
            cursor = conn.cursor()
            id =len(cursor.execute("""SELECT post_id FROM Posts""").fetchall())+1
            cursor.execute("""INSERT INTO Posts VALUES (?, ?, ?) """, (id, title, content,))
            



# # print(DataBase.opened_post(2))
# # print(DataBase.get_all_posts(10))
# DataBase.init_db()


