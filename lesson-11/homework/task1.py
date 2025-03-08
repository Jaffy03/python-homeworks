import sqlite3

#1 Database creation
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT, 
    Species TEXT, 
    Age INT
    )""")
conn.commit()

#2 Insert data
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

conn.commit()

#3 Update data
cursor.execute('UPDATE Roster SET Name = "Ezri Dax" WHERE Name = "Jadzia Dax"')
conn.commit()

#4 Query Data
cursor.execute('SELECT Name, Age FROM Roster WHERE Species = "Bajoran"')
bajoran = cursor.fetchall()
print("Bajoran Data: ")
for name, age in bajoran:
    print(f"Name: {name}, Age: {age}")

#5 Delete Data
cursor.execute('DELETE FROM Roster WHERE Age>100')
conn.commit()

