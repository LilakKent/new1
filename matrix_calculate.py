from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import numpy as np

Builder.load_file("multiscreen.kv")

class MultiScreenApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.calculator_screen = CalculatorScreen(name='calculator')
        self.matrix_calculator_screen = MatrixCalculatorScreen(name='matrix_calculator')
        self.menu_screen = MenuScreen(name='menu')

        self.sm.add_widget(self.menu_screen)
        self.sm.add_widget(self.calculator_screen)
        self.sm.add_widget(self.matrix_calculator_screen)

        return self.sm

    def switch_screen(self, screen_name):
        self.sm.current = screen_name

class CalculatorScreen(Screen):
    pass
    # def add_cal(self):
    #     self.expression = ''
    #     return self.root
    #
    # def update_input(self, value):
    #     # Обрабатываем ввод мнимой единицы "j" и добавляем ее к выражению
    #     if value == 'j':
    #         self.expression += 'j'
    #     else:
    #         self.expression += str(value)
    #     self.root.ids.input_field.text = self.expression
    #
    # def clear_input(self):
    #     self.expression = ''
    #     self.root.ids.input_field.text = ''
    #
    # def calculate_result(self):
    #     try:
    #         # Используйте функцию eval с помощью комплексных чисел
    #         result = eval(self.expression, {'__builtins__': None}, {"j": 1j})
    #         self.expression = str(result)
    #         self.root.ids.input_field.text = self.expression
    #     except Exception:
    #         self.root.ids.input_field.text = 'Error'

class MatrixCalculatorScreen(Screen):
    def add_matrices(self):
        try:
            matrix_a_str = self.ids.matrix_a.text
            matrix_b_str = self.ids.matrix_b.text

            # Преобразование строк в numpy матрицы
            matrix_a = np.array(eval(matrix_a_str))
            matrix_b = np.array(eval(matrix_b_str))

            # Сложение матриц
            result_matrix = matrix_a + matrix_b

            # Отображение результата
            self.ids.result_label.text = str(result_matrix)
        except Exception as e:
            self.ids.result_label.text = 'Ошибка'

class MenuScreen(Screen):
    pass

if __name__ == '__main__':
    app = MultiScreenApp()
    app.run()
