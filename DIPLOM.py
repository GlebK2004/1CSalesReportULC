import matplotlib.pyplot as plt

# Данные
seasons = ['Весна 2023', 'Лето 2023', 'Осень 2023', 'Зима 23-24', 'Весна 2024', 'Лето 2024', 'Осень 2024']
values = [5848, 5066, 8847, 11935, 14531, 14138, 15253]

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(seasons, values, marker='o', color='#FF7273', linewidth=2, markersize=8)


# Настройка графика
plt.title('Количество проведённых занятий', fontsize=16)
# plt.xlabel('Сезоны', fontsize=12)
# plt.ylabel('Значения', fontsize=12)
plt.xticks(rotation=45)
#plt.grid(True)

# Установка пределов оси Y с отступами
plt.ylim(min(values) - 4000, max(values) + 2000)  # Увеличим диапазон оси Y
# Убрать обозначения на оси Y
plt.yticks([])

# # Добавление подписей к точкам
# for i, value in enumerate(values):
#     plt.text(seasons[i], value + 200, str(value), ha='center', fontsize=10, color='black')

# Показать график
plt.tight_layout()
plt.show()