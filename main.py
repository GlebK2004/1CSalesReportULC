# Чтение данных из Excel-файла
from builtins import dict, zip, print, sorted
from collections import defaultdict


from data_file import count_sales, all_managers
from pie_charts import pie_charts
from sales_by_threes import sales_by_threes
from total_income import total_income

# count_sales()
# all_managers()
# pie_charts()
# total_income()
# sales_by_threes()

import numpy as np
from scipy.optimize import minimize

# Исходные значения
S1 = 59925.5
S2 = 573503.1
S3 = 179079.0
S4 = 347418.5
current_P = 0.03 * (S1 + S2 + S3 + S4)

# Функция для вычисления P
def objective(x):
    k1, k2, k3, k4 = x
    return abs(k1 * S1 + k2 * S2 + k3 * S3 + k4 * S4 - current_P)

# Ограничения: k2 > k3 + 0.005, k1 > k2, k2 > k3, k3 > k4
def constraint1(x):
    return x[1] - x[2] - 0.005  # k2 - k3 >= 0.005

def constraint2(x):
    return x[0] - x[1]  # k1 > k2

def constraint3(x):
    return x[1] - x[2]  # k2 > k3

def constraint4(x):
    return x[2] - x[3]  # k3 > k4

# Начальные приближения для коэффициентов
x0 = np.array([0.03, 0.03, 0.03, 0.03])  # Все коэффициенты равны 0.03

# Ограничения
constraints = [{'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2},
               {'type': 'ineq', 'fun': constraint3},
               {'type': 'ineq', 'fun': constraint4}]

# Границы для коэффициентов (коэффициенты должны быть положительными)
bounds = [(0, None), (0, None), (0, None), (0, None)]

# Оптимизация
result = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)

# Вывод результатов
if result.success:
    new_coefficients = result.x
    new_P = new_coefficients[0] * S1 + new_coefficients[1] * S2 + new_coefficients[2] * S3 + new_coefficients[3] * S4
    percent_change = ((new_P - current_P) / current_P) * 100

    print("Оптимизированные коэффициенты:", new_coefficients)
    print("Новое значение P:", new_P)
    print("Изменение в процентах:", percent_change)
else:
    print("Оптимизация не удалась:", result.message)

