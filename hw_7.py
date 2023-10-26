import sqlite3   

def bazza(db_name): 
    connectoin = sqlite3.connect(db_name)
    return connectoin

bazza("hw.db")

def table(conn,sql): 
    cursor = conn.cursor()
    cursor.execute(sql)

def create_products(conn,product: tuple):
    sql = """INSERT INTO products
    (product_tittle, price, quantity)
    VALUES (?,?,?);
    """
    cursor = conn.cursor()
    cursor.execute(sql, product)
    conn.commit()
    
def delet_product(conn,id: int): 
    sql = '''DELETE FROM products WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()    

    
sql_table = """
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_tittle VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0 
);
"""
connection = bazza("hw.db")
if connection:
    print("успешное соединение")
    table(connection, sql_table)
    create_products(connection,("Apple", 100.00, 120))
    create_products(connection,("SAMSUNG", 100.00, 120))
    delet_product(connection, 1)
    

