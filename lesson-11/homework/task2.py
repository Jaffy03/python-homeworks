import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INT,
    Genre TEXT 
)               
'''
)
conn.commit()

data = [
    ('To KIll a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')        
]
cursor.executemany('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES(?, ?, ?, ?)', data)
conn.commit()

cursor.execute('UPDATE Books SET Year_Published = 1950 WHERE Title = "1984"')
conn.commit()

cursor.execute('SELECT Title, Author FROM Books WHERE Genre = "Dystopian"')
dystopian = cursor.fetchall()

print('Dystopian Books: ')
for title, author in dystopian:
    print(f"Title: {title}, Author: {author}")

cursor.execute('DELETE FROM Books WHERE Year_Published < 1950')
conn.commit()    