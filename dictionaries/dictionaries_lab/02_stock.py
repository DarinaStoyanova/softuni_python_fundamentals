products = input().split(" ")

dict_products = {}

for index in range(0,len(products), 2):
    key = products[index]
    value = products[index+1]
    dict_products[key] = int(value)

products_to_search_for = input().split(" ")

for product in products_to_search_for:
    if product in dict_products:
        print(f"We have {dict_products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
