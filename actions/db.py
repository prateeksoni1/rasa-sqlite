import sqlite3

conn = sqlite3.connect('rasa.db')

print("connected")

class Repo:

  @staticmethod
  def initDb():
    conn.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            EMPLOYEE_CODE TEXT UNIQUE NOT NULL,
            EMAIL TEXT UNIQUE NOT NULL
        );
    ''')
    print("table created")

  
  @staticmethod
  def insert(name, emp_code, email):
    conn.execute('''
      INSERT INTO candidates (NAME, EMPLOYEE_CODE, EMAIL) VALUES (?, ?, ?);
    ''', (name, emp_code, email))

  @staticmethod
  def select():

    cur = conn.cursor()

    cur.execute('''
      SELECT * FROM candidates;
    ''')

    rows = cur.fetchall()

    return str(rows).strip('[]') if len(rows) > 0 else "No records found"

  @staticmethod
  def delete(value):

    name = value + "%"

    conn.execute('''
      DELETE FROM candidates WHERE name like ? OR employee_code like ?
    ''', (name, value,))