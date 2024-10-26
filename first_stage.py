# Чтение данных из Excel-файла
from builtins import dict, zip, print, sorted
from collections import defaultdict
import pandas as pd

# Список файлов для обработки
files = [
    'D:\\Глеб\\Underground\\Менеджеры графики\\Август24.xls',
    'D:\\Глеб\\Underground\\Менеджеры графики\\Июнь24.xls',
    'D:\\Глеб\\Underground\\Менеджеры графики\\Июль24.xls'
    # Добавьте другие файлы по мере необходимости
]

# Инициализация массивов для сумм
total_online_ind = []
total_offline_ind = []
total_online_group = []
total_offline_group = []

# Обработка каждого файла
for file in files:
    df = pd.read_excel(file, header=0)

    data = defaultdict(list)
    for _, row in df.iterrows():
        name = row['Номенклатура абонемента']
        value = row['Сумма']
        data[name].append(value)

    # Локальные суммы для текущего файла
    online_ind = 0
    offline_ind = 0
    online_group = 0
    offline_group = 0

    for name, values in data.items():
        total = sum(values)
        if "сплит" not in name.lower():
            if "online" in name.lower() and "инд" in name.lower():
                online_ind += total
            if "online" in name.lower() and "групп" in name.lower():
                online_group += total
            if "online" not in name.lower() and "инд" in name.lower():
                offline_ind += total
            if "online" not in name.lower() and "групп" in name.lower():
                offline_group += total

    # Добавление локальных сумм в массивы
    total_online_ind.append(online_ind)
    total_offline_ind.append(offline_ind)
    total_online_group.append(online_group)
    total_offline_group.append(offline_group)

# Вывод итоговых сумм
print(f"Суммы онлайн индивидуальных: {total_online_ind}")
print(f"Суммы оффлайн индивидуальных: {total_offline_ind}")
print(f"Суммы онлайн групповых: {total_online_group}")
print(f"Суммы оффлайн групповых: {total_offline_group}")

# Общие суммы
total_online_ind_sum = sum(total_online_ind)
total_offline_ind_sum = sum(total_offline_ind)
total_online_group_sum = sum(total_online_group)
total_offline_group_sum = sum(total_offline_group)
print(f"Общая сумма онлайн индивидуальных: {sum(total_online_ind)}")
print(f"Общая сумма оффлайн индивидуальных: {sum(total_offline_ind)}")
print(f"Общая сумма онлайн групповых: {sum(total_online_group)}")
print(f"Общая сумма оффлайн групповых: {sum(total_offline_group)}")

k_default = 0.03
sum_managers_1 = k_default * (total_offline_ind_sum + total_online_ind_sum + total_online_group_sum + total_offline_group_sum)
print("Отчисления менеджерам до:", sum_managers_1)

k_off_ind = 0.025
k_on_ind = 0.025
k_off_gr = 0.03
k_on_gr = 0.035

sum_managers_2 = (k_off_ind * total_offline_ind_sum +
                  k_on_ind * total_online_ind_sum +
                  k_off_gr * total_offline_group_sum +
                  k_on_gr * total_online_group_sum)
print("Отчисления менеджерам после:", sum_managers_2)

difference = sum_managers_2/sum_managers_1*100 - 100
print("Отчисления изменились на:", difference, "%")



