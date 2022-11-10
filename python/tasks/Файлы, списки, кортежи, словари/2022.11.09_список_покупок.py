# Вы отправились в магазин и попросили друзей составить список покупок и прислать его вам.
# Каждый из друзей написал свой список и в итоге вам прислали три файла: shopping_list_1.txt, shopping_list_2.txt и shopping_list_3.txt.
# Когда вы открыли списки покупок, то сразу заметили, что некоторые товары повторяются,
# поэтому вы решили составить свой собственный нормализованный список, где продукты не повторяются и записаны по алфавиту.
#
# Напишите программу shopping_list.py, которая читает строки из трех файлов:
# shopping_list_1.txt, shopping_list_2.txt и
# shopping_list_3.txt, а затем создает новый файл shopping_list.txt,
# в который помещает все прочитанные строки без повторов и в алфавитном порядке.
#
# Примечание: все исходные списки заканчиваются пустой строкой.

def shopping_list(file_name):
    file_n = open(f"{file_name}")
    f = file_n.read()
    return f
    file_n.close()

product_list_files = ["shopping_list_1.txt", "shopping_list_2.txt", "shopping_list_3.txt"]
full_products = []

for i in product_list_files:
    full_products += shopping_list(i).split("\n")


full_products = list(set(full_products))
full_products.sort()
full_products = full_products[1:]

full_products_file = open("shopping_list.txt", "w")
full_products_file.write('\n'.join(full_products))
full_products_file.close()
# full_products_file = open("full_products_file.txt")
# print(full_products_file.read())