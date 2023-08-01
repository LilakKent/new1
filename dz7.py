# def filter_and_limit_string(input_string):
#     result_list = []  # Створюємо пустий список, куди будемо додавати букви
#     count = 0  # Лічильник доданих букв
#
#     i = 0
#     while i < len(input_string) and count < 100:
#         letter = input_string[i]
#         if letter.lower() not in ('m', 'n'):  # Перевіряємо, чи літера не 'm' або 'n' (регістр не має значення)
#             result_list.append(letter)
#             count += 1
#         i += 1
#
#     return result_list
#
# input_string = input("Введіть рядок: ")
# filtered_list = filter_and_limit_string(input_string)
# print("Результат:", filtered_list)



import unittest
def main_function():
    time = t
    speed = v
    weight = m


    while time < 0:
        raise ValueError('Write something > 0')
    while speed < 0:
        raise ValueError('Write something > 0')
    while weight < 0:
        raise ValueError('Write something > 0')



t = int(input('Enter time: '))
v = int(input('Enter speed ur car: '))
m = int(input('Enter weight of ur car: '))

print(f'A vehicle weighing {m} kg moved for {t} seconds at a speed of {v} m/s and covered a distance of 30 meters')
main_function()
class test(unittest.TestCase):
    def test_function(self):
        result = main_function(arguments)
        self.assertEqual(result, expected_result)

    if __name__ == '__main__':
        unittest.main()
