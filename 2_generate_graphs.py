import csv, datetime, collections
import matplotlib.pyplot as plt

def get_months_values_amounts():
    sales = csv.reader(open('data_clean.csv'))
    sales.__next__() # remove header

    values = {}
    amounts = {}
    for sale in sales:
        amnt = float(sale[4])
        price = float(sale[5])
        month = datetime.datetime.strptime(sale[1], "%Y-%m-%d").month

        if(month in values):
            values[month] += amnt * price
            amounts[month] += amnt
        else:
            values[month] = amnt * price
            amounts[month] = amnt

    return values, amounts

if __name__ == "__main__":
    months_values, months_amounts = get_months_values_amounts()

    ord_values = collections.OrderedDict(sorted(months_values.items()))
    ord_amounts = collections.OrderedDict(sorted(months_amounts.items()))

    months = ord_values.keys()
    values = ord_values.values()
    amounts = ord_amounts.values()

    plt.plot(months, values, label='Value')
    plt.title('Total Sales Value per Month')
    plt.xlabel('Month')
    plt.ylabel('Total value (R$)')
    plt.legend()
    plt.savefig('monthly_sales_value.png', dpi=300)
    plt.show()

    plt.plot(months, amounts, label='Amount')
    plt.title('Total Amount of Sales per Month')
    plt.xlabel('Month')
    plt.ylabel('Total amount')
    plt.legend()
    plt.savefig('monthly_sales_amount.png', dpi=300)
    plt.show()
  