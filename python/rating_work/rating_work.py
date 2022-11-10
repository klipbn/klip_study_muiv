# Создаем файл с начальными условиями для задачи
source_list = []
for i in range(-17, 6):
    source_list.append(f"x={i}")
source_data = open("source_data.txt", "w", encoding="UTF-8")
source_data.write("\n".join(source_list))
source_data.close()

# читаем исходные данные из файла, преобразую строки в целочисленные значения
source_data_txt = open("source_data.txt", "r", encoding="UTF-8")
source_data_list = source_data_txt.read().replace("x=", "").split()
source_data_list = [int(j) for j in source_data_list]
source_data_txt.close()

print(source_data_list)

result_list = []

for x in source_data_list:
    try:
        if x < -7:
            y = (76 * x ** 2) / (20 * x ** 3)
            result_list.append(f"При х = {x} значение y = {y:.3f}")
        elif -7 <= x < -1:
            y = (76 * x ** 2) / (20 * x ** 3)
            result_list.append(f"При х = {x} значение y = {y:.3f}")
        else:
            y = (76 * x ** 2) / (20 * x ** 3)
            result_list.append(f"При х = {x} значение y = {y:.3f}")
    except:
        result_list.append(f"При х = {x} значение y = ∞")
print(result_list)

result_data = open("result.txt", "w", encoding="UTF-8")
result_data.write("\n".join(result_list))
result_list.close()