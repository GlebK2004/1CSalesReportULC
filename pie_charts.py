import matplotlib.pyplot as plt
from data_file import data

def pie_charts():
    import matplotlib.pyplot as plt

    # Подсчитываем суммы для абонементов с и без слова "Online"
    online_sum = 0
    non_online_sum = 0
    for name, values in data.items():
        total = sum(values)
        if "online" in name.lower():
            online_sum += total
        else:
            non_online_sum += total

    # Строим круговую диаграмму для Online/Offline
    fig1, ax1 = plt.subplots(figsize=(6, 6.2))
    labels1 = ['Online', 'Offline']
    sizes1 = [online_sum, non_online_sum]
    patches1, texts1, autotexts1 = ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=90)
    # Увеличиваем размер меток и значений
    for t in texts1:
        t.set_fontsize(14)
    for t in autotexts1:
        t.set_fontsize(14)
    ax1.axis('equal')
    ax1.set_title('Распределение дохода по формату абонементов', fontsize=16)
    plt.tight_layout()
    plt.savefig('online_offline_distribution.png', dpi=300, format='png')
    plt.show()

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
    fig2, ax2 = plt.subplots(figsize=(6, 6.2))
    labels2 = ['Инд', 'Групп']
    sizes2 = [individual_sum, group_sum]
    patches2, texts2, autotexts2 = ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=70)
    # Увеличиваем размер меток и значений
    for t in texts2:
        t.set_fontsize(14)
    for t in autotexts2:
        t.set_fontsize(14)
    ax2.axis('equal')
    ax2.set_title('Распределение дохода по типу абонементов', fontsize=16)
    plt.tight_layout()
    plt.savefig('individual_group_distribution.png', dpi=300, format='png')
    plt.show()


pie_charts()

