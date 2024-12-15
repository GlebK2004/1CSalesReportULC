import matplotlib.pyplot as plt
from data_file import data


def chinese_bar():

    # Подсчитываем суммы для абонементов с и без слова "Кит"
    chinese_sum = 0
    other_sum = 0
    for name, values in data.items():
        total = sum(values)
        if "кит" in name.lower():
            chinese_sum += total
        else:
            other_sum += total

    # Строим круговую диаграмму для Китайский/Другие
    fig1, ax1 = plt.subplots(figsize=(6, 6.2))
    labels1 = ['Китайский', '']
    sizes1 = [chinese_sum, other_sum]
    patches1, texts1, autotexts1 = ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=30)
    # Увеличиваем размер меток и значений
    for t in texts1:
        t.set_fontsize(14)
    for t in autotexts1:
        t.set_fontsize(14)
    ax1.axis('equal')
    ax1.set_title('Доля китайского языка', fontsize=16)  # Установите размер шрифта заголовка
    plt.tight_layout()
    plt.savefig('chinese_distribution.png', dpi=300, format='png', bbox_inches='tight')
    plt.show()

    # Подсчитываем суммы для абонементов с и без слова "груп"
    child_sum = 0
    gr_sum = 0
    for name, values in data.items():
        total = sum(values)
        if "груп" in name.lower():
            if "детск" in name.lower():
                child_sum += total
            else:
                gr_sum += total

    # Строим круговую диаграмму для Детские/Взрослые
    fig2, ax2 = plt.subplots(figsize=(6, 6.2))  # Увеличьте размер до 8x8 дюймов
    labels2 = ['Детские', 'Взрослые']
    sizes2 = [child_sum, gr_sum]
    patches2, texts2, autotexts2 = ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=30)
    # Увеличиваем размер меток и значений
    for t in texts2:
        t.set_fontsize(14)
    for t in autotexts2:
        t.set_fontsize(14)
    ax2.axis('equal')
    ax2.set_title('Детские/взрослые групповые абонементы', fontsize=16)  # Установите размер шрифта заголовка
    plt.tight_layout()
    plt.savefig('children_group_distribution.png', dpi=300, format='png', bbox_inches='tight')
    plt.show()



chinese_bar()