import sqlite3

def init_db():
    connection = sqlite3.connect('app\\database\\test.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users( 'id' INTEGER PRIMARY KEY,
        'username' TEXT NOT NULL,
        'email' TEXT NOT NULL)
        
                    """)
    connection.commit()
    connection.close()

def add_user():
    pass

def post():
    pass


init_db()