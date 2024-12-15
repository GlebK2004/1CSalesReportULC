# Чтение данных из Excel-файла
from builtins import dict, zip, print, sorted
import matplotlib.pyplot as plt

from data_file import add_space_every_3_digits, df


def total_income():
    trio1 = ['Аксёнова Екатерина', 'Михалкин Виктор', 'Перхова Ангелина']
    trio2 = ['Ризаева Виктория', 'Неведомская Анастасия', 'Коробко Александр']
    trio3 = ['Зарецкая Юлия', 'Чудук Александр', 'Данилов Дмитрий']
    trio4 = ['Мурзич Павлина', 'Новосад Марина', 'Лавринович Ирина']

    # Находим доход по менеджерам
    data_summ = {}

    # Создаем список всех троек
    all_trios = [trio1, trio2, trio3, trio4]

    for name, value in zip(df['Заявка.Ответственный'], df['Сумма']):
        if value != 1.00:
            # Проверяем, к какой тройке принадлежит менеджер
            for trio in all_trios:
                if name in trio:
                    # Суммируем значения для тройки
                    trio_key = tuple(trio)  # Ключем будет кортеж тройки
                    if trio_key in data_summ:
                        data_summ[trio_key] += value
                    else:
                        data_summ[trio_key] = value
                    break  # Выход из цикла, если менеджер найден в одной из троек

    # Новый словарь с другими именами для троек
    new_data_summ = {}

    # Пример: задаем новые имена для троек
    new_names = {
        'Михалкин и Перхова \n (Аксёнова)': tuple(trio1),
        'Неведомская и Коробко \n (Ризаева)': tuple(trio2),
        'Данилов и Чудук \n (Зарецкая)': tuple(trio3),
        'Лавринович и Новосад \n (Мурзич)': tuple(trio4)
    }

    # Заполняем новый словарь
    for new_name, trio_key in new_names.items():
        total = data_summ.get(trio_key, 0)  # Получаем сумму или 0, если тройка нет в data_summ
        new_data_summ[new_name] = total

    # Сортируем данные по значениям
    sorted_data = sorted(new_data_summ.items(), key=lambda item: item[1], reverse=True)

    # Извлекаем надписи
    trios = [trio for trio, _ in sorted_data]
    sums = [value for _, value in sorted_data]

    # Создаем вертикальный столбчатый график с размером 16:9
    plt.figure(figsize=(16, 9))
    plt.subplots_adjust(left=0.1, right=0.98, top=0.94, bottom=0.1)  # Убираем отступы
    bars = plt.bar(trios, sums)  # Изменено на plt.bar()
    #plt.ylabel('Общий доход', fontsize=18)  # Изменено на ylabel
    plt.title('Суммарный доход', fontsize=22)
    plt.grid(axis='y')

    # Добавляем подписи для каждой полосы с пробелами между цифрами
    for bar in bars:
        formatted_value = add_space_every_3_digits(bar.get_height())
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 formatted_value,
                 ha='center', va='bottom', fontsize=20)

    # Настройка меток на оси X
    plt.xticks(rotation=0, fontsize=18)  # Поворачиваем метки по оси X для удобства чтения
    # Устанавливаем пределы для оси Y
    # plt.ylim(0, 230000)  # Устанавливаем максимальное значение на оси Y
    # Отображаем график
    plt.savefig('sum_income.png', dpi=300, format='png', bbox_inches='tight')
    plt.show()


total_income()