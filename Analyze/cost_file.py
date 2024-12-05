import matplotlib.pyplot as plt

# Данные
months = ['Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август']
values = [1837, 2141, 1823, 2175, 998, 2559]

# Создание столбчатой диаграммы
plt.figure(figsize=(16, 9))
plt.bar(months, values)

# Добавление заголовка и меток
plt.title('Расходы на аудитории', fontsize=18)
plt.xlabel('Месяцы', fontsize=16)
plt.ylabel('Сумма (BYN)', fontsize=16)
plt.xticks(fontsize=16)

# Отображение значений над столбцами
for i, value in enumerate(values):
    plt.text(i, value + 30, str(value), ha='center', fontsize=16)

# Показать диаграмму
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Данные
months = ['Апрель', 'Май', 'Июнь', 'Июль', 'Август']
values = [2353, 2140, 2010, 2180, 2012]

# Создание столбчатой диаграммы
plt.figure(figsize=(16, 9))
plt.bar(months, values)

# Добавление заголовка и меток
plt.title('Кол-во оффлайн-занятий', fontsize=18)
plt.xticks(fontsize=16)

# Отображение значений над столбцами
for i, value in enumerate(values):
    plt.text(i, value + 30, str(value), ha='center', fontsize=16)

# Показать диаграмму
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()