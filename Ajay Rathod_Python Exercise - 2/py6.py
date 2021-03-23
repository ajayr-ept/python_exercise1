# Create a program that read a .csv file and print its data in dictionary
# Data is about Sales Order
# The dictionary should have SO number as key and its values as dictionaries
# {SO001 :
# {‘customer’ : {‘name’:<customer name>,‘address 1’ : <value of address1>,’address 2’: <value of
# address 2>, ‘city’ :<city>, ‘country’: <country>},
# ’Products’:[
# {‘sku’:<sku>,’price’:<price>,’qty’:<qty>},
# {‘sku’:<sku>,’price’:<price>}
# ]
# }
# }
# There should be a provision in the program where code of country is converted to country’s full
# name and only full name of country  should be stored in a dictionary.
# Use import csv library for managing csv task
import csv
orderdic = {}

with open("data.csv", 'r') as file:
    # read csv file
    data = csv.DictReader(file)
    for row in data:
        # check header is available or not
        if row.get("Order No") == 'Order No':
            continue
        # check repeted data if not then update dictionary
        if row["Order No"] not in orderdic:
            orderdic.update({
                row["Order No"]: {'Customer': {'Name':row['Customer'],
                                 'Address1': row['Address1'],
                                 'Address2': row['Address2'],
                                 'City': row['City'],
                                 'Country': row['Country'],
                                 'ZipCode': row['Zipcode']},
                    'Products': [{'Quantity': row['Qty'],'SKU': row['SKU'],'Price': row['Price']}]
                }})
        # if order no is same then append list at last of list of dictionary of same customer
        else:
             orderdic.get(row['Order No']).get('Products').append({'Quantity': row['Qty'],
                'SKU': row['SKU'],
                'Price': row['Price']
            })


# print the dictionary
print(orderdic)

