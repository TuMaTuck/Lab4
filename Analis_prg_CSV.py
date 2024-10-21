import csv
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Читання CSV файлу
employees = []
try:
    with open('employees.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаємо заголовок
        for row in reader:
            birth_date = datetime.strptime(row[4], '%Y-%m-%d')
            age = calculate_age(birth_date)
            employees.append([row[3], age])  # Стать і вік
    print("Ok")
except FileNotFoundError:
    print("Файл CSV не знайдено!")
    exit()

# Статистика за статтю
gender_counts = Counter([emp[0] for emp in employees])
print(f"Чоловіки: {gender_counts['Чоловіча']}, Жінки: {gender_counts['Жіноча']}")

# Побудова діаграми за статтю
labels = 'Чоловіки', 'Жінки'
sizes = [gender_counts['Чоловіча'], gender_counts['Жіноча']]
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Розподіл за статтю')
plt.show()

# Статистика за віковими категоріями
age_categories = {"<18": 0, "18-45": 0, "45-70": 0, ">70": 0}
for _, age in employees:
    if age < 18:
        age_categories["<18"] += 1
    elif 18 <= age <= 45:
        age_categories["18-45"] += 1
    elif 45 < age <= 70:
        age_categories["45-70"] += 1
    else:
        age_categories[">70"] += 1

print("Кількість співробітників за віковими категоріями:", age_categories)

# Побудова діаграми за віковими категоріями
plt.figure(figsize=(8, 6))
plt.bar(age_categories.keys(), age_categories.values(), color='skyblue')
plt.title('Розподіл за віковими категоріями')
plt.xlabel('Категорії віку')
plt.ylabel('Кількість')
plt.show()
