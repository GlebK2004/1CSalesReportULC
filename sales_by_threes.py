# Чтение данных из Excel-файла
from builtins import dict, zip, print, sorted
from collections import defaultdict
import openpyxl
from openpyxl.styles import Font
import pandas as pd
import matplotlib.pyplot as plt

from data_file import data, df



def sales_by_threes():

    df1 = pd.read_excel('D:\\Глеб\\Underground\\Менеджеры графики\\Цены_на_продукты06.12.xls', header=0)
    # Создаем словарь с парами имя - число
    dataPrice = {}
    for _, row in df1.iterrows():
        name = row['Номенклатура']
        value = row['Цена']
        dataPrice[name] = value  # Сохраняем последнее значение для каждого имени

    df = pd.read_excel('D:\\Глеб\\Underground\\Менеджеры графики\\25-30.11.24.xls', header=0)
    # Определяем группы
    trios = [
        ['Аксёнова Екатерина', 'Михалкин Виктор', 'Перхова Ангелина'],
        ['Ризаева Виктория', 'Неведомская Анастасия', 'Коробко Александр'],
        ['Зарецкая Юлия', 'Чудук Александр', 'Данилов Дмитрий'],
        ['Мурзич Павлина', 'Новосад Марина', 'Лавринович Ирина']
    ]

    new_names = [
        'Михалкин и Перхова \n (Аксёнова)',
        'Неведомская и Коробко \n (Ризаева)',
        'Данилов и Чудук \n (Зарецкая)',
        'Лавринович и Новосад \n (Мурзич)'
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
    unique_products = df1["Номенклатура"].unique()

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
                    if key in dataPrice:
                        if value != 1.00:
                            if value / dataPrice[key] >= 0.6:
                                product_dict[key] += 1
                            else:
                                product_dict[key] += round(value / dataPrice[key], 2)

        # Создание словаря с названиями строк и значениями
        result_dict = {key: product_dict[key] for key in product_dict}

        # Запись итогового словаря в список
        product_dict_list.append(result_dict)

        # Сортируем словарь product_dict по убыванию значений
        sorted_product_dict = dict(sorted(product_dict.items(), key=lambda x: x[1], reverse=True))

        # Удаляем продукты с количеством 0 из отсортированного словаря
        sorted_product_dict = {k: v for k, v in sorted_product_dict.items() if v > 1}

        # Задайте список ключей, которые нужно удалить
        keys_to_remove = ['Online 1 инд. зан. (1р.)', '1 инд. зан. (1р.)']

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
            plt.text(v, i, round(v, 2), color='black', va='center', fontsize=18)

        # Отображаем диаграмму
        plt.tight_layout()
        plt.show()

    # Создание DataFrame из списка словарей
    df = pd.DataFrame(product_dict_list)
    # Транспонирование DataFrame, чтобы строки стали столбцами и наоборот
    df_transposed = df.T
    # Создание заголовков для первых 5 столбцов
    header = ['Продукт',
              'Михалкин и Перхова',
              'Неведомская и Коробко',
              'Данилов и Чудук',
              'Лавринович и Новосад']
    # Проверяем количество столбцов и создаем заголовки
    num_cols = len(df_transposed.columns)
    if num_cols > 0:
        # Используем заголовки, как только они соответствуют количеству столбцов
        if num_cols <= len(header):
            df_transposed.columns = header[:num_cols]  # Устанавливаем заголовки по количеству столбцов
        else:
            # Если заголовков больше, чем столбцов, добавляем пустые строки для остальных
            df_transposed.columns = header + [''] * (num_cols - len(header))
    # Запись заголовков в отдельный файл без индекса
    header_df = pd.DataFrame(columns=header)
    header_df.to_excel('product_dict_list_transposed.xlsx', header=False, index=False,  engine='openpyxl')

    # Запись основного DataFrame с индексом
    df_transposed.to_excel('product_dict_list_transposed.xlsx', header=True, index=True, engine='openpyxl')

sales_by_threes()






