product_list = {}

def add_product(product_list, product_name, product_quantity):
    if product_name in product_list:
        product_list[product_name] += product_quantity
    else:
        product_list[product_name] = product_quantity

def show_product(product_list):
    for key in product_list.keys():
        print(key + " : " + str(product_list[key]))

add_product(product_list, "Tomato", 20)
add_product(product_list, "Chips", 15)
add_product(product_list, "Milk", 15)
show_product(product_list)
