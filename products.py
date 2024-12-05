# Получение массива всех уникальных значений столбца "Номенклатура абонемента"
from matplotlib import pyplot as plt
from data_file import df, data


def products():
    # Находим общую выручку по абонементам
    data_summ = {}
    for name, value in zip(df['Номенклатура абонемента'], df['Сумма']):
        if value != 1.00:
            if name in data_summ:
                data_summ[name] += value
            else:
                data_summ[name] = value

    # Сортируем значения и продукты в порядке убывания
    sorted_product_dict_summ = dict(sorted(data_summ.items(), key=lambda x: x[1], reverse=True))

    # Настраиваем размеры фигуры
    fig, ax = plt.subplots(figsize=(16, 9))

    # Строим горизонтальную столбчатую диаграмму в обратном порядке
    ax.barh(list(reversed(list(sorted_product_dict_summ.keys())[:15])),
            list(reversed(list(sorted_product_dict_summ.values())[:15])), align='center')

    # Устанавливаем метки для осей
    ax.set_xlabel('Сумма, BYN')
    # ax.set_ylabel('Абонемент')
    ax.set_title('Наиболее прибыльные абонементы за первое полугодие 2024 года', fontsize=15)

    # Функция для добавления пробелов между 3 цифрами
    def add_space_every_3_digits(number):
        number_str = str(int(number))
        result = ''
        for i, digit in enumerate(reversed(number_str)):
            if i > 0 and i % 3 == 0:
                result = ' ' + result
            result = digit + result
        return result

    # Отображаем значения на столбцах в обратном порядке
    for i, v in enumerate(list(sorted_product_dict_summ.values())[:15]):
        ax.text(v, list(reversed(list(sorted_product_dict_summ.keys())[:15]))[-(i + 1)], add_space_every_3_digits(v),
                color='black', ha='left', va='center', fontsize=12)

    # Растягиваем диаграмму на всю фигуру
    fig.tight_layout()

    # Показываем диаграмму
    plt.show()



products()


