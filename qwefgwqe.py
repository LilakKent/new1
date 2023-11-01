"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку
здійснюється за механізмом
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення,
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
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
# ваш код нижче !!!!!!!! вище нічого не змінюємо
import random as rn

num_list = []
total_grades = 0
count = 0
student_GPA = []
student_number = []

# while len(num_list) < 1:
#     num = str(rn.randint(0, 999999999)).zfill(9)
#     if not num in num_list:
#         num_list.append(num)


student = {
    'Степан Гасанов': {
        'Пошта': 'Stepan@gmail.com',
        'Вік': 20,
        'Номер телефону': '+420708245858',
        'Середній бал': 76.6
    },
}
students.update(student)

for number_students, infor in students.items():
    if 'Номер телефону' in infor and infor['Номер телефону'] is None:

        random_phone = str(rn.randint(0, 999999999)).zfill(9)
        infor['Номер телефону'] = f'+{random_phone}'

# students['Женя Курич']['Номер телефону'] = '+420608245858'

for student_s, info in students.items():
    if 'Середній бал' in info and info['Середній бал'] > 90:
        student_GPA.append({
            'Імя': student_s,
            'Середній бал': info['Середній бал']
        })

for student_s in student_GPA:
    print(f'{student_s["Імя"]} - Середній бал: {student_s["Середній бал"]}')

for student_info in students.values():
    if 'Середій бал' in student_info:
        total_grades += student_info['Середній бал']
        count += 1

for student_info in students.values():
    if 'Середній бал' in student_info:
        total_grades += student_info['Середній бал']
        count += 1

average_grade = total_grades / count

print(f'Середній бал по групі: {average_grade}')
print(students['Женя Курич']['Номер телефону'])
