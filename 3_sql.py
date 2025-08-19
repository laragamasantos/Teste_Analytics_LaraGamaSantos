from pathlib import Path
import pandas as pd
import numpy as np
import sqlite3

def create_database(c):
    c.execute('''CREATE TABLE sales (ID int, Date text, Product text, Category text, Amount int, Price real)''')

    sales = pd.read_csv('data_clean.csv')
    sales.to_sql('sales', conn, if_exists='append', index = False)

def execute_sql_commands(c):
    res = c.execute('''SELECT Product, Category, ROUND(SUM(Amount*Price),2) AS TotalSales FROM sales
                        GROUP BY Product
                        ORDER BY TotalSales DESC
                    ''').fetchall()

    print(np.array(res))

if __name__ == "__main__":
    # Connect to database
    Path('ecommerce.db').touch()
    conn = sqlite3.connect('ecommerce.db')
    connection = conn.cursor()

    create_database(connection)

    execute_sql_commands(connection)