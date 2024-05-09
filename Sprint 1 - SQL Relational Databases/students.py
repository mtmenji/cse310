import sqlite3

# Open connection with SQLite
connection = sqlite3.connect("grade_six.db")
cursor = connection.cursor()

##### CREATION OF THE DATABASE #####
# Create tables for the database.
cursor.execute("CREATE TABLE student (id INTEGER PRIMARY KEY, name TEXT, gender TEXT, age INTEGER, gpa REAL)")
cursor.execute("CREATE TABLE history (name TEXT, assignment TEXT, grade REAL)")
cursor.execute("CREATE TABLE algebra (name TEXT, assignment TEXT, grade REAL)")
cursor.execute("CREATE TABLE football (name TEXT, position TEXT, starter BOOL)")
cursor.execute("CREATE TABLE dance (name TEXT, style TEXT, height REAL)")
cursor.execute("CREATE TABLE band (name TEXT, instrument TEXT, style TEXT)")
# Create arrays with information.
student_roster = [
    ("Michael", "M", 12, 3.12),
    ("Hailey", "F", 11, 4.00),
    ("Jackie", "F", 12, 2.5),
    ("Trevor", "M", 12, 3.54),
    ("Sheila", "F", 12, 3.95),
    ("Daniel", "M", 11, 2.45),
    ("Millie", "F", 11, 4.00),
    ("Oliver", "M", 10, 3.90),
    ("Jackson", "M", 12, 2.32),
    ("Layla", "F", 12, 2.75)
]
history_class = [
    ("Michael", "Homework 1", 90),
    ("Hailey", "Homework 1", 100),
    ("Jackie", "Homework 1", 77),
    ("Trevor", "Homework 1", 85),
    ("Sheila", "Homework 1", 95),
    ("Daniel", "Homework 1", 68),
    ("Millie", "Homework 1", 100),
    ("Oliver", "Homework 1", 99),
    ("Jackson", "Homework 1", 0),
    ("Layla", "Homework 1", 50),
    ("Michael", "Homework 2", 80),
    ("Hailey", "Homework 2", 95),
    ("Jackie", "Homework 2", 68),
    ("Trevor", "Homework 2", 88),
    ("Sheila", "Homework 2", 93),
    ("Daniel", "Homework 2", 73),
    ("Millie", "Homework 2", 100),
    ("Oliver", "Homework 2", 95),
    ("Jackson", "Homework 2", 65),
    ("Layla", "Homework 2", 71),
    ("Michael", "Homework 3", 90),
    ("Hailey", "Homework 3", 100),
    ("Jackie", "Homework 3", 70),
    ("Trevor", "Homework 3", 78),
    ("Sheila", "Homework 3", 94),
    ("Daniel", "Homework 3", 0),
    ("Millie", "Homework 3", 100),
    ("Oliver", "Homework 3", 100),
    ("Jackson", "Homework 3", 80),
    ("Layla", "Homework 3", 0),
    ("Michael", "Test 1", 75),
    ("Hailey", "Test 1", 95),
    ("Jackie", "Test 1", 68),
    ("Trevor", "Test 1", 79),
    ("Sheila", "Test 1", 90),
    ("Daniel", "Test 1", 69),
    ("Millie", "Test 1", 97),
    ("Oliver", "Test 1", 100),
    ("Jackson", "Test 1", 65),
    ("Layla", "Test 1", 42)
]
algebra_class = [
    ("Michael", "Variable Equations HW", 93),
    ("Hailey", "Variable Equations HW", 94),
    ("Jackie", "Variable Equations HW", 70),
    ("Trevor", "Variable Equations HW", 89),
    ("Sheila", "Variable Equations HW", 98),
    ("Daniel", "Variable Equations HW", 62),
    ("Millie", "Variable Equations HW", 100),
    ("Oliver", "Variable Equations HW", 91),
    ("Jackson", "Variable Equations HW", 0),
    ("Layla", "Variable Equations HW", 0),
    ("Michael", "Variable Equations Quiz", 84),
    ("Hailey", "Variable Equations Quiz", 91),
    ("Jackie", "Variable Equations Quiz", 73),
    ("Trevor", "Variable Equations Quiz", 88),
    ("Sheila", "Variable Equations Quiz", 96),
    ("Daniel", "Variable Equations Quiz", 68),
    ("Millie", "Variable Equations Quiz", 90),
    ("Oliver", "Variable Equations Quiz", 93),
    ("Jackson", "Variable Equations Quiz", 74),
    ("Layla", "Variable Equations Quiz", 72),
    ("Michael", "Exponents HW", 94),
    ("Hailey", "Exponents HW", 100),
    ("Jackie", "Exponents HW", 73),
    ("Trevor", "Exponents HW", 0),
    ("Sheila", "Exponents HW", 99),
    ("Daniel", "Exponents HW", 78),
    ("Millie", "Exponents HW", 100),
    ("Oliver", "Exponents HW", 100),
    ("Jackson", "Exponents HW", 80),
    ("Layla", "Exponents HW", 0),
    ("Michael", "Exponents Quiz", 72),
    ("Hailey", "Exponents Quiz", 99),
    ("Jackie", "Exponents Quiz", 61),
    ("Trevor", "Exponents Quiz", 71),
    ("Sheila", "Exponents Quiz", 90),
    ("Daniel", "Exponents Quiz", 80),
    ("Millie", "Exponents Quiz", 94),
    ("Oliver", "Exponents Quiz", 100),
    ("Jackson", "Exponents Quiz", 70),
    ("Layla", "Exponents Quiz", 45)
]
football_roster = [
    ("Michael", "RB", 0),
    ("Trevor", "QB", 1),
    ("Daniel", "WR", 1)
]
dance_roster = [
    ("Hailey", "Classical", 4.00),
    ("Jackie", "Contemporary", 2.5),
    ("Millie", "Hip Hop", 4.00),
    ("Oliver", "Tap", 3.90)
]
band_roster = [
    ("Michael", "Saxophone", "Jazz"),
    ("Hailey", "Piano", "Broadway"),
    ("Oliver", "Drums", "Rock"),
    ("Jackson", "Guitar", "Country"),
    ("Layla", "Trumpet", "Jazz")
]
# Enter arrays into the tables of the database.
cursor.executemany("INSERT INTO student(name, gender, age, gpa) VALUES (?,?,?,?)", student_roster)
cursor.executemany("INSERT INTO history VALUES (?,?,?)", history_class)
cursor.executemany("INSERT INTO algebra VALUES (?,?,?)", algebra_class)
cursor.executemany("INSERT INTO football VALUES (?,?,?)", football_roster)
cursor.executemany("INSERT INTO dance VALUES (?,?,?)", dance_roster)
cursor.executemany("INSERT INTO band VALUES (?,?,?)", band_roster)

##### Utilizing the Database to Acheive Results #####
# Demonstrate which student has the highest average grade in history:
for row in cursor.execute("SELECT name, MAX(average) FROM(SELECT name, AVG(grade) AS average FROM history GROUP BY name)"):
    print(row)

# To be in band, you need a minimum GPA of 3.00. Remove any band students not meeting this requirement:
for row in cursor.execute("SELECT b.* FROM band b JOIN student s ON b.name = s.name WHERE s.GPA >= 3.00"):
    print(row)

# Output a list of students who are in multiple extracurriculars:
for row in cursor.execute("SELECT name, COUNT(*) AS occurrences FROM (SELECT name FROM football UNION ALL SELECT name FROM dance UNION ALL SELECT name FROM band) AS all_names GROUP BY name HAVING COUNT(*) > 1"):
    print(row)

# Close connection with SQLite
connection.close()