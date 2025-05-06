
import sqlite3
def get_connection():
    return sqlite3.connect("inventory.db")
DB_NAME="inventory_db"
def connect():
    try:
        con = sqlite3.connect(DB_NAME)
        return con
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_table():
    con=connect()
    cur=con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS inventory(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
                )
                
''')
    con.commit()
    con.close()

def check_data():
    con=sqlite3.connect('inventory.db')
    cr=con.cursor()
    cr.execute("SELECT * FROM inventory")
    print(cr.fetchall())

    con.close()
#functions to get all items
def get_all_items():
    con = sqlite3.connect(DB_NAME)
    cr =con.cursor()
    cr.execute('SELECT * FROM inventory')
    items=cr.fetchall()
    con.close()
    return items

#function to add inventory
def add_items(name,qty,price):
    con=sqlite3.connect(DB_NAME)
    cr=con.cursor()
    cr.execute('INSERT INTO inventory(name,quantity,price)VALUES(%s,%s,%s)',(name,qty,price))
    con.commit()
    con.close()


#fuction to delete 
def delete_item(item_id):
    con=sqlite3.connect(DB_NAME)
    cr=con.cursor()
    cr.execute('DELETE FROM inventory WHERE id=?',(item_id,))
    con.commit()
    con.close()


#function to get based on ID
def get_item_by_id(item_id):
    con=sqlite3.connect(DB_NAME)
    cr=con.cursor()
    cr.execute('SELECT * FROM inventory WHERE id=?',(item_id,))
    con.close()


#functio to update
def update_items(item_id,name,qty,price):
    con = sqlite3.connect(DB_NAME)
    cr=con.cursor()
    cr.execute('UPDATE inventory SET name=?,quatity=?,price=? WHERE id=?,(name,qty,price,item_id)')
    con.commit()
    con.close()


if __name__=="__main__":
    create_table()
    check_data()