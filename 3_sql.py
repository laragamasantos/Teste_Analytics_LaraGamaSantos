from pathlib import Path
import pandas as pd
import numpy as np
import sqlite3

def create_database(c):
    c.execute('''CREATE TABLE sales (ID int, Date text, Product text, Category text, Amount int, Price real)''')

    sales = pd.read_csv('data_clean.csv')
    sales.to_sql('sales', conn, if_exists='append', index = False)

def execute_sql_commands(c):
    res1 = c.execute('''SELECT Product, Category, ROUND(SUM(Amount*Price),2) AS TotalSales FROM sales
                        GROUP BY Product
                        ORDER BY TotalSales DESC
                    ''').fetchall()

    print("Consulta 1:")
    print(np.array(res1))

    res2 = c.execute('''SELECT Product, Category, SUM(Amount) AS AmountOfSales, strftime('%m', Date) AS Month FROM sales
                        WHERE Month = '06'
                        GROUP BY Product
                        ORDER BY AmountOfSales DESC
                    ''').fetchall()

    print()
    print("Consulta 2:")
    print(np.array(res2))

if __name__ == "__main__":
    # Connect to database
    Path('ecommerce.db').touch()
    conn = sqlite3.connect('ecommerce.db')
    connection = conn.cursor()

    create_database(connection)

    execute_sql_commands(connection)