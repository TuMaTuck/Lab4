import csv
from faker import Faker
import random

# Ініціалізація Faker з українською локалізацією
fake = Faker('uk_UA')

# Словники для По батькові
male_middle_names = [
    "Олександрович", "Іванович", "Петрович", "Сергійович", "Андрійович",
    "Михайлович", "Володимирович", "Дмитрович", "Юрійович", "Богданович"
]
female_middle_names = [
    "Олександрівна", "Іванівна", "Петрівна", "Сергіївна", "Андріївна",
    "Михайлівна", "Володимирівна", "Дмитрівна", "Юріївна", "Богданівна"
]

# Встановлення пропорцій
num_records = 2000
male_percentage = 0.6
female_percentage = 0.4
num_males = int(num_records * male_percentage)
num_females = num_records - num_males

# Функція для генерації співробітників
def generate_employee(gender):
    if gender == 'M':
        first_name = fake.first_name_male()
        middle_name = random.choice(male_middle_names)
        gender_str = "Чоловіча"
    else:
        first_name = fake.first_name_female()
        middle_name = random.choice(female_middle_names)
        gender_str = "Жіноча"
    
    last_name = fake.last_name()
    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, middle_name, gender_str, birth_date, position, city, address, phone, email]

# Генерація і збереження даних у CSV
with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

    # Запис чоловіків
    for _ in range(num_males):
        writer.writerow(generate_employee('M'))

    # Запис жінок
    for _ in range(num_females):
        writer.writerow(generate_employee('F'))

print("CSV файл успішно створено!")
