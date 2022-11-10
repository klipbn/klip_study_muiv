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

result_list = []

# создадим лист с результатом, добавим в него значения согласно условию
# формат вывода сделаем через exp с округлением до 3 знаков, согласно условию
for x in source_data_list:
    try:
        if x < -7:
            y = ((76 * x ** 6 + 50 * x ** 2 + 51) ** 8 - 38 * x ** 8) / (
                    (15 * x ** 3 - x ** 3) ** 7 + (16 * x ** 2 + 12) ** 4)
            result_list.append(f"При х = {x} значение y = {y:.3e}")
        elif -7 <= x < -1:
            y = (((37 * x ** 4 + 80 * x ** 2 + 92) ** 5) ** 0.5) / (
                    (59 * x ** 6 + x ** 2) ** 5 + (25 * x ** 2 - 38) ** 6)
            result_list.append(f"При х = {x} значение y = {y:.3e}")
        else:
            y = ((5 * x ** 5 + 78 * x ** 2 + 75) ** 6 - 11 * x ** 5) / (
                    (7 * x ** 6 - x ** 3) ** 5 + ((38 * x - 79) ** 3) ** 0.5)
            result_list.append(f"При х = {x} значение y = {y:.3e}")
    except:
        result_list.append(f"При х = {x} значение y = ∞")

# сохраним файл результата
result_data = open("result.txt", "w", encoding="UTF-8")
result_data.write("\n".join(result_list))
result_data.close()
