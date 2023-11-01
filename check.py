import random as rn

num_list = []
total_grades = 0
count = 0
student_GPA = []
student_number = []

while len(num_list) < 1:
    num = str(rn.randint(0, 999999999)).zfill(9)
    if num not in num_list:
        num_list.append(num)

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

for student_name, student_info in students.items():
    if 'Номер телефону' in student_info and student_info['Номер телефону'] is None:
        random_phone = str(rn.randint(0, 999999999)).zfill(9)
        student_info['Номер телефону'] = f'+{random_phone}'

print(students['Женя Курич']['Номер телефону'])