import numpy as np
import pandas as pd
import datetime, random, csv
from collections import namedtuple

prod_struct = namedtuple("prod_struct", "name categ price")

products = [
    prod_struct("Nintendo Switch", "Entertainment", 4013.00),
    prod_struct("Puzzle", "Entertainment", 64.67),
    prod_struct("TV", "Entertainment", 2469.05),
    prod_struct("Uno", "Entertainment", 13.79),
    prod_struct("Blender", "Kitchen", 180.41),
    prod_struct("Air Fryer", "Kitchen", 284.05),
    prod_struct("Refrigerator", "Kitchen", 4465.05),
    prod_struct("Pan", "Kitchen", 179.90),
    prod_struct("Hairdryer", "Beauty", 226.22),
    prod_struct("Eyeliner", "Beauty", 64.97),
    prod_struct("Cleansing Oil", "Beauty", 147.57),
    prod_struct("Eyeshadow Palette", "Beauty", 380.00),
    prod_struct("Volleyball", "Sports", 74.90),
    prod_struct("Tennis Racket", "Sports", 999.89),
    prod_struct("Tennis Ball Kit", "Sports", 34.90),
    prod_struct("Bicycle", "Sports", 1671.80),
    prod_struct("Dress", "Clothing", 219.90),
    prod_struct("T-Shirt", "Clothing", 80.00),
    prod_struct("Socks", "Clothing", 14.99),
    prod_struct("Sweatshirt", "Clothing", 119.90),
]

def get_product():
    return random.choice(products)
    

def generate_dataset(num_sales, start_date, end_date):
    ids = np.arange(1,num_sales+1)
    
    dates = []
    products = []
    categories = []
    prices = []
    amounts = []
    for _ in range(num_sales):
        # create entries
        time_betw_dates = end_date - start_date
        days_betw_dates = time_betw_dates.days
        random_num_days = random.randrange(days_betw_dates)
        random_date = start_date + datetime.timedelta(days=random_num_days)
        dates.append(random_date.strftime("%Y-%m-%d"))

        product = get_product()
        products.append(product.name)
        categories.append(product.categ)
        prices.append(product.price)
        
        amounts.append(random.randint(1, 5))    

    # create dataframe
    data = {
        "ID": ids,
        "Date": dates,
        "Product": products,
        "Category": categories,
        "Amount": amounts,
        "Price": prices
    }
    sales_df = pd.DataFrame(data)

    # generate csv 
    sales_df.to_csv("data_clean.csv", index=False)

def get_total_and_amount():
    csv_data = csv.reader(open('data_clean.csv'))
    csv_data.__next__() # skip first row

    total_values = {}
    total_amounts = {}
    for sale in csv_data:
        name = sale[2]
        amnt = float(sale[4])
        price = float(sale[5])

        if(name in total_values):
            total_values[name] += amnt * price
            total_amounts[name] += amnt
        else:
            total_values[name] = amnt * price
            total_amounts[name] = amnt

    return total_values, total_amounts

if __name__ == "__main__":
    num_sales = 50
    start_date = datetime.datetime.strptime("2023-01-01", "%Y-%m-%d")
    end_date = datetime.datetime.strptime("2023-12-31", "%Y-%m-%d")

    generate_dataset(num_sales, start_date, end_date)

    total_values, total_amounts = get_total_and_amount()

    print("Total de vendas por produto:")
    for elem in total_values.items():
        print(" - " + elem[0] + " por R$ %.2f" % elem[1])

    best_sell = max(total_amounts.items(), key=lambda item: item[1])

    print()
    print("O item mais vendido foi: " + best_sell[0] + ", com um total de %.0f vendas" % best_sell[1])
    print()
