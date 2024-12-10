import matplotlib.pyplot as plt
from data_file import data


def chinese_bar():
    # Подсчитываем суммы для абонементов с и без слова "Online"
    chinese_sum = 0
    other_sum = 0
    for name, values in data.items():
        total = sum(values)
        if "кит" in name.lower():
            chinese_sum += total
        else:
            other_sum += total

    # Строим круговую диаграмму для Online/Offline
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    labels = ['Китайский', ' ']
    sizes = [chinese_sum, other_sum]
    patches, texts, autotexts = ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    # Increase the size of the labels and values
    for t in texts:
        t.set_fontsize(14)
    for t in autotexts:
        t.set_fontsize(14)
    ax1.axis('equal')
    ax1.set_title('Доля китайского языка')

    # Подсчитываем суммы для абонементов с и без слова "инд"
    child_sum = 0
    gr_sum = 0
    for name, values in data.items():
        total = sum(values)
        if "груп" in name.lower():
            if "детск" in name.lower():
                child_sum += total
            else:
                gr_sum += total

    # Строим круговую диаграмму для Групповые/Индивидуальные
    labels = ['Детские', 'Взрослые']
    sizes = [child_sum, gr_sum]
    patches, texts, autotexts = ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    # Increase the size of the labels and values
    for t in texts:
        t.set_fontsize(14)
    for t in autotexts:
        t.set_fontsize(14)
    ax2.axis('equal')
    ax2.set_title('Детские/взрослые групповые абонементы')
    plt.tight_layout()
    plt.show()

 



chinese_bar()