import matplotlib.pyplot as plt
from data_file import data

def pie_charts():
    # Подсчитываем суммы для абонементов с и без слова "Online"
    online_sum = 0
    non_online_sum = 0
    for name, values in data.items():
        total = sum(values)
        if "сплит" not in name.lower():
            if "online" in name.lower():
                online_sum += total
            else:
                non_online_sum += total

    # Строим круговую диаграмму для Online/Offline
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    labels = ['Online', 'Offline']
    sizes = [online_sum, non_online_sum]
    patches, texts, autotexts = ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    # Increase the size of the labels and values
    for t in texts:
        t.set_fontsize(14)
    for t in autotexts:
        t.set_fontsize(14)
    ax1.axis('equal')
    ax1.set_title('Распределение доходов по Online/Offline')

    # Подсчитываем суммы для абонементов с и без слова "инд"
    group_sum = 0
    individual_sum = 0
    for name, values in data.items():
        total = sum(values)
        if "инд" in name.lower():
            individual_sum += total
        else:
            group_sum += total

    # Строим круговую диаграмму для Групповые/Индивидуальные
    labels = ['Индивидуальные', 'Групповые']
    sizes = [individual_sum, group_sum]
    patches, texts, autotexts = ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    # Increase the size of the labels and values
    for t in texts:
        t.set_fontsize(14)
    for t in autotexts:
        t.set_fontsize(14)
    ax2.axis('equal')
    ax2.set_title('Распределение доходов по типам абонементов')
    plt.tight_layout()
    plt.show()


