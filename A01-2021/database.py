import sqlite3

#Open database
conn = sqlite3.connect('database.db')

# wesh bonne question
c = conn.cursor()

#Create table
c.execute('''CREATE TABLE users 
            (id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            isadmin BOOLEAN
            )''')

# Insert data in database
c.execute('''
INSERT INTO users VALUES (1, 'admin', '5f32116d116fd77a584163459294e183', true)
''')

c.execute('''
INSERT INTO users VALUES (2, 'test', '098f6bcd4621d373cade4e832627b4f6', false)
''')

c.execute('''
INSERT INTO users VALUES (3, 'guest', '084e0343a0486ff05530df6c705c8bb4', false)
''')

c.execute('''
INSERT INTO users VALUES (4, 'bob', 'db046d11906b9f9baeaec687d853543c', false)
''')

c.execute('''
INSERT INTO users VALUES (5, 'alice', 'e8179ef7b94585e19cb02420370d6a8c', false)
''')

conn.commit()