import sqlite3
 
def tables():
    connection = sqlite3.connect('week13.db')
 
    sql_query = """SELECT name FROM sqlite_master
    WHERE type='table';"""
 
    tables = connection.cursor()
     
    tables.execute(sql_query)
    print("Tables in db\n")
     
    print(tables.fetchall())
 
    connection.close()






def fields():
    connection = sqlite3.connect('week13.db')

    sql_query = "SELECT * FROM cars"

    tables = connection.cursor()

    tables.execute(sql_query)
    print("Fields in Table\n")

    print(tables.fetchall())

    connection.close()


def max():
    connection = sqlite3.connect('week13.db')

    sql_query = "SELECT MAX (Price) FROM cars"

    tables = connection.cursor()

    tables.execute(sql_query)
    print("Max Price in Price\n")

    print(tables.fetchall())

    connection.close()


def min():
    connection = sqlite3.connect('week13.db')

    sql_query = "SELECT MIN (Price) FROM cars"

    tables = connection.cursor()

    tables.execute(sql_query)
    print("Min Price in Price\n")

    print(tables.fetchall())

    connection.close()



tables()
fields()
max()
min()
