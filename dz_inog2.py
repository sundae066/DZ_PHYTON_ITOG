import matplotlib.pyplot as plt
import numpy as np

# Пример данных
# Предположим, что у вас есть массивы возраста и баллов по расходам
ages = np.array([22, 25, 27, 30, 32, 35, 37, 40, 45, 50])
spending_scores = np.array([60, 70, 75, 80, 85, 90, 70, 65, 55, 50])

# Построение линейного графика
plt.figure(figsize=(10, 6))
plt.plot(ages, spending_scores, marker='o')
plt.title('Зависимость расходов от возраста')
plt.xlabel('Возраст')
plt.ylabel('Баллы по расходам')
plt.grid()
plt.xticks(ages)  # Устанавливаем метки по оси X
plt.yticks(range(0, 101, 10))  # Устанавливаем метки по оси Y
plt.show()