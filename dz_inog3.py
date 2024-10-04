import matplotlib.pyplot as plt

# Пример данных
salaries = [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]
bonuses = [5000, 6000, 7000, 8000, 9000, 10000, 12000, 15000, 18000, 20000]
years_at_company = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Построение точечного графика
plt.figure(figsize=(10, 6))
scatter = plt.scatter(salaries, bonuses, s=[year * 20 for year in years_at_company], alpha=0.5)
plt.title('Взаимосвязь между зарплатой и бонусами')
plt.xlabel('Зарплата')
plt.ylabel('Бонусы')
plt.grid()

# Добавление аннотации для размера точек
for i in range(len(years_at_company)):
    plt.annotate(f'{years_at_company[i]}', (salaries[i], bonuses[i]), fontsize=9, ha='right')

plt.show()