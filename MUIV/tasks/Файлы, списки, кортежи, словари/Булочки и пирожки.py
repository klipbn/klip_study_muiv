# import sys
# food = sys.argv[1]
# l = food.split(",")
#
#
# l_new = []
# for i in range(len(l)):
#     if i == 0 and (len(l) > 2):
#         l_new.append(l[i].title())
#         l_new.append(", ")
#     elif i == 0 and (len(l) <= 2):
#         l_new.append(l[i].title())
#         l_new.append(" и ")
#     elif i == (len(l) - 1):
#         l_new.append(l[i])
#         l_new.append(".")
#     elif i == (len(l) - 2):
#         l_new.append(l[i])
#         l_new.append(" и ")
#     elif i < (len(l) - 1) and i != 0:
#         l_new.append(l[i])
#         l_new.append(", ")
#
# print("".join(l_new))


import sys

# Разбиваем полученные данные с помощью split().
products = sys.argv[1].split(",")

# Склеиваем строку из элементов списка исключая последний элемент.
products_str = ", ".join(products[:-1])

# Последний элемент присоединяем к строке через союз "и".
products_str = products_str + " и " + products[-1] + "."

# Применяем capitalize() и выводим результат.
print(products_str.capitalize())