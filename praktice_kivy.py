from kivy.app import App

from kivy.lang import Builder

# Builder.load_file("calculator.kv")

class CalculatorApp(App):
    def build(self):
        self.expression = ''
        return self.root

    def update_input(self, value):
        # Обрабатываем ввод мнимой единицы "j" и добавляем ее к выражению
        if value == 'j':
            self.expression += 'j'
        else:
            self.expression += str(value)
        self.root.ids.input_field.text = self.expression

    def clear_input(self):
        self.expression = ''
        self.root.ids.input_field.text = ''

    def calculate_result(self):
        try:
            # Используйте функцию eval с помощью комплексных чисел
            result = eval(self.expression, {'__builtins__': None}, {"j": 1j})
            self.expression = str(result)
            self.root.ids.input_field.text = self.expression
        except Exception:
            self.root.ids.input_field.text = 'Error'

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()





# from kivy.app import App
# from kivy.lang import Builder
#
# Builder.load_file("calculator.kv")
#
# class CalculatorApp(App):
#     def build(self):
#         self.expression = ''
#         return self.root
#
#     def update_input(self, value):
#         self.expression += str(value)
#         self.root.ids.input_field.text = self.expression
#
#     def clear_input(self):
#         self.expression = ''
#         self.root.ids.input_field.text = ''
#
#     def calculate_result(self):
#         try:
#             self.expression = str(eval(self.expression))
#             self.root.ids.input_field.text = self.expression
#         except Exception:
#             self.root.ids.input_field.text = 'Error'
#
# if __name__ == '__main__':
#     app = CalculatorApp()
#     app.run()














































# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
#
# class CalculatorApp(App):
#     def build(self):
#         self.expression = ''
#         self.result = TextInput(font_size=32, readonly=True, multiline=False)
#         return BoxLayout(orientation='vertical', padding=10, spacing=10, children=[self.result])
#
#     def update_input(self, value):
#         self.expression += str(value)
#         self.result.text = self.expression
#
#     def clear_input(self):
#         self.expression = ''
#         self.result.text = ''
#
#     def calculate_result(self):
#         try:
#             self.expression = str(eval(self.expression))
#             self.result.text = self.expression
#         except Exception:
#             self.result.text = 'Error'
#
# if __name__ == '__main__':
#     app = CalculatorApp()
#     app.run()




# def build1(self):
    #
    #     return Builder.load_file("main.kv")

# from kivy.app import App
#
# class MyApp(App):
#     def build(self):
#         return Builder.load_file("main.kv")
#
#     def on_button_click(self):
#         button = self.root.ids.my_button
#         button.text = "Кнопка была нажата!"
#
# if __name__ == "__main__":
#     MyApp().run()
