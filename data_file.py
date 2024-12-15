# Чтение данных из Excel-файла
from builtins import dict, zip, print, sorted
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('D:\\Глеб\\Underground\\Менеджеры графики\\21-30Ноября24.xls', header=0)

data = defaultdict(list)
for _, row in df.iterrows():
    name = row['Номенклатура абонемента']
    value = row['Сумма']
    data[name].append(value)

# Функция для добавления пробелов между 3 цифрами
def add_space_every_3_digits(number):
    number_str = str(int(number))
    result = ''
    for i, digit in enumerate(reversed(number_str)):
        if i > 0 and i % 3 == 0:
            result = ' ' + result
        result = digit + result
    return result

# проверка на пустые строчки
# nan_rows = df[df["Номенклатура абонемента"].isna()].index
# print(nan_rows)

def count_sales():
    # Считаем, сколько всего было оплат
    print("Количество записей:", len(df['Номенклатура абонемента']))

def all_managers():
    # Получение массива всех уникальных значений столбца "Номенклатура абонемента"
    managers = df["Заявка.Ответственный"].unique()
    print("Менеджеры, вносившие оплату:", managers)


