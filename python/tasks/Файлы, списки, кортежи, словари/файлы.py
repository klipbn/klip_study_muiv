new_products_files = open("new_shopping_list.txt", "w") # "+r"
new_products_files.write("молоко\nсуп")
new_products_files.close()

products_files = open("shopping_list.txt", encoding="utf8") #cp1251
products = products_files.read().strip()
products = products.replace("масло\n", "").title()
print(products)