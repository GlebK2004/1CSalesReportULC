# Чтение данных из Excel-файла
from builtins import dict, zip, print, sorted
from collections import defaultdict
import openpyxl
from openpyxl.styles import Font
import pandas as pd
import matplotlib.pyplot as plt

from data_file import data, df



def sales_by_threes():

    df1 = pd.read_excel('D:\\Глеб\\Underground\\Менеджеры графики\\Цены_на_продукты.xls', header=0)
    # Создаем словарь с парами имя - число
    data1 = defaultdict(list)
    for _, row in df1.iterrows():
        name = row['Номенклатура']
        value = row['Цена']
        data1[name].append(value)

    df = pd.read_excel('D:\\Глеб\\Underground\\Менеджеры графики\\25-30.11.24.xls', header=0)
    # Определяем группы
    trios = [
        ['Бровко Екатерина', 'Перхова Ангелина', 'Михалкин Виктор'],
        ['Новосад Марина', 'Данилов Дмитрий', 'Мурзич Павлина'],
        ['Зарецкая Юлия', 'Чудук Александр', 'Лавринович Ирина']
    ]
    new_names = [
        'Михалкин | Перхова - Бровко',
        'Данилов | Новосад - Мурзич',
        'Чудук | Лавринович - Зарецкая'
    ]

    # Создаем словарь с парами имя - список [число, заявка]
    data = defaultdict(list)

    for _, row in df.iterrows():
        name = row['Номенклатура абонемента']
        value = row['Сумма']
        request = row['Заявка.Ответственный']  # Получаем значение из столбца 'Заявка'

        # Добавляем кортеж (или список) в словарь
        data[name].append((value, request))  # Сохраняем сумму и заявку как кортеж

    # Получение массива всех уникальных значений столбца "Номенклатура абонемента"
    unique_products = df["Номенклатура абонемента"].unique()

    # Итоговый двумерный массив
    product_dict_list = []

    # Проходим по словарю data и считаем продажи
    for i, trio in enumerate(trios):

        # Создание словаря с уникальными значениями в качестве ключей и числом 0 в качестве значений
        product_dict = {product: 0 for product in unique_products}

        for key, value_list in data.items():
            for value, request in value_list:
                if request in trio:
                    # Проверяем, есть ли цена для данного продукта в data1
                    if key in data1:
                        # Получаем половину цены (если есть)
                        half_price = min(data1[key]) / 2  # Берем минимальную цену, если несколько
                        if value > half_price:
                            product_dict[key] += 1

        # Создание словаря с названиями строк и значениями
        result_dict = {key: product_dict[key] for key in product_dict}

        # Запись итогового словаря в список
        product_dict_list.append(result_dict)

        # Сортируем словарь product_dict по убыванию значений
        sorted_product_dict = dict(sorted(product_dict.items(), key=lambda x: x[1], reverse=True))

        # Удаляем продукты с количеством 0 из отсортированного словаря
        sorted_product_dict = {k: v for k, v in sorted_product_dict.items() if v > 1}

        # Задайте список ключей, которые нужно удалить
        keys_to_remove = ['Online - 1 инд (1р.)', '1 индивидуальное занятие (1р.)', 'Online - 1 инд ', 'VIP_вз']

        # Удаляем записи по указанным ключам
        for key in keys_to_remove:
            if key in sorted_product_dict:
                del sorted_product_dict[key]

        # Извлекаем ключи и значения из обновленного отсортированного словаря
        products = list(sorted(sorted_product_dict.keys(), key=lambda x: sorted_product_dict[x], reverse=False))
        values = [sorted_product_dict[p] for p in products]

        # Определяем количество значений для отображения
        num_display = 10

        # Получаем последние 10 значений для диаграммы
        display_products = products[-num_display:]
        display_values = values[-num_display:]

        # Создаем DataFrame для всех значений
        all_data = pd.DataFrame({
            'Продукты': products,
            'Количество': values
        })

        # Настраиваем размеры фигуры
        plt.figure(figsize=(16, 9))

        # Строим горизонтальную столбчатую диаграмму
        plt.barh(range(len(display_products)), display_values, align='center')

        # Устанавливаем метки для осей
        plt.yticks(range(len(display_products)), display_products, fontsize=16)
        plt.xlabel('Количество')
        name = new_names[i]
        plt.title(f'Абонементы за месяц: {name}', fontsize=18)

        # Отображаем значения на столбцах
        for i, v in enumerate(display_values):
            plt.text(v, i, str(v), color='black', va='center', fontsize=18)

        # Отображаем диаграмму
        plt.tight_layout()
        plt.show()

    # Создание DataFrame из списка словарей
    df = pd.DataFrame(product_dict_list)
    # Транспонирование DataFrame, чтобы строки стали столбцами и наоборот
    df_transposed = df.T
    # Запись транспонированного DataFrame в файл Excel
    df_transposed.to_excel('product_dict_list_transposed.xlsx', header=False)


sales_by_threes()






